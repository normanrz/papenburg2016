import json
import sys
import re
import gzip
from functools import reduce

internal_links_re = re.compile("\[\[([^\]]+)\]\]")
external_links_re = re.compile("\[([a-z]+:[^\]\s]+)\s+([^\]]+)\]")
cross_links_re = re.compile("\{\{([^\}]+)\}\}")
html_tags_re = re.compile("<[^>]+>")
filter_title_re = re.compile("^(File:|User:|Talk:|User talk:|Template:|User blog comment:|User blog:|Category:)")


def load_wikidata(filename):
    if filename.endswith(".gz"):
        return load_wikidata_gzip(filename)
    else:
        return load_wikidata_normal(filename)


def load_wikidata_normal(filename):
    with open(filename, "rt", encoding="UTF-8") as f:
        for line in f:
            doc = json.loads(line)
            if not filter_title(doc["title"]):
                doc["byteOffset"] = 0
                yield doc


def load_wikidata_gzip(filename):
    with gzip.open(filename, "rt", encoding="UTF-8") as f:
        for line in f:
            doc = json.loads(line)
            if not filter_title(doc["title"]):
                doc["byteOffset"] = 0
                yield doc


def filter_title(title):
    return bool(filter_title_re.match(title))


def find_internal_links(doc_text):
    return map(lambda a: a.group(1), internal_links_re.finditer(doc_text))


def multi_sub(re_list, replacement, subject):
    return reduce(lambda r, a: re.sub(a, replacement, r), re_list, subject)


def clean_wikidata(doc_text):
    return \
        re.sub(external_links_re, lambda m: m.group(2),
               re.sub(internal_links_re, lambda m: m.group(1),
                      multi_sub([html_tags_re, cross_links_re], "", doc_text)))


def load_wikidata_texts(filename):
    for doc in load_wikidata(filename):
        yield clean_wikidata(doc["text"])
