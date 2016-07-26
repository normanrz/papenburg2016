import json
import sys
import re
import gzip
from functools import reduce

internal_links_re = re.compile("\[\[([^\]]+)\]\]")
external_links_re = re.compile("\[([a-z]+:[^\]\s]+)\s+([^\]]+)\]")
cross_links_re = re.compile("\{\{([^\}]+)\}\}")
html_tags_re = re.compile("<[^>]+>")


def load_wikidata(filename):
    with open(filename, "rt", encoding="UTF-8") as f:
        for line in f:
            doc = json.loads(line)
            doc["byteOffset"] = 0
            yield doc


def load_wikidata_gzip(filename):
    with gzip.open(filename, "rt", encoding="UTF-8") as f:
        for line in f:
            doc = json.loads(line)
            doc["byteOffset"] = 0
            yield doc


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


if __name__ == "__main__":
    for _doc in load_wikidata_gzip(sys.argv[1]):
        print(clean_wikidata(_doc["text"]))
