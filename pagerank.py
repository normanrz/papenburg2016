import numpy as np
import pickle
from os import path
from load_dataset import load_wikidata, find_internal_links
from build_index import filename
from collections import Counter


def convert_title(link):
    div_pos = link.find('|')
    if div_pos != -1:
        return link.lower()[:div_pos]
    else:
        return link.lower()

#filename = path.join("datasets", "pokemon_pages_current.json.gz")
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)
doc_titles = set(map(convert_title, doc_titles))

# Tut mir leid. Bin ich gewoehnt.
all_links = set()
num_docs = 0
docid_of_doctitle = {}
doctitle_of_docid = {}
d_global = 0.85
adj_list = []
num_links = []
pagerank_values_old = []
pagerank_values = []

def gather_sites():
    for doc_no, doc in enumerate(load_wikidata(filename)):
        links = find_internal_links(doc["text"])
        for link in links:
            linktext = convert_title(link)
            if linktext in doc_titles:
                all_links.add(linktext)

def build_docid_mapping():
    global num_docs
    for link in all_links:
        if link not in docid_of_doctitle:
            docid_of_doctitle[link] = num_docs
            doctitle_of_docid[num_docs] = link
            num_docs += 1

def build_adj_list():
    global adj_list, num_links
    adj_list = [[] for i in range(num_docs)]
    num_links = np.zeros(num_docs)
    done = set()
    for doc_no, doc in enumerate(load_wikidata(filename)):
        if convert_title(doc["title"]) not in all_links: continue
        own_title = convert_title(doc["title"])
        if (docid_of_doctitle[own_title] in done): continue
        links = set(map(convert_title, find_internal_links(doc["text"]))).intersection(all_links)
        num_links[docid_of_doctitle[own_title]] = len(links)
        for link in links:
            adj_list[docid_of_doctitle[link]].append(docid_of_doctitle[own_title])
        done.add(docid_of_doctitle[own_title])

def calc_pagerank_head():
    global pagerank_values, pagerank_values_old
    initial_value = 1.0 / num_docs
    pagerank_values_old = [initial_value for i in range(num_docs)]
    pagerank_values = [0 for i in range(num_docs)]
    for i in range(100):
        update_pagerank_arr()

def update_pagerank_arr():
    global pagerank_values, pagerank_values_old
    for i in range(num_docs):
        update_pagerank_value(i)
    pagerank_values_old = pagerank_values


def update_pagerank_value(index):
    global pagerank_values, pagerank_values_old
    pagerank_values[index] = (1.0-d_global) / num_docs
    sum_pr = 0
    for j in adj_list[index]:
        sum_pr += pagerank_values_old[j]/num_links[j]
    pagerank_values[index] += sum_pr * d_global

gather_sites()
build_docid_mapping()
build_adj_list()
calc_pagerank_head()
pagerank_final_values = [(i, pagerank_values[i]) for i in range(num_docs)]

pagerank_mapping = {}
for site in pagerank_final_values:
    pagerank_mapping[doctitle_of_docid[site[0]]] = site[1]

with open("pagerank.pickle", "wb") as f:
    pickle.dump(pagerank_mapping, f)
print("done")
