import numpy as np
import pickle
from os import path
from load_dataset import load_wikidata, find_internal_links
from build_index import filename


# global variables
all_links = set()
num_docs = 0
docid_of_doctitle = {}
doctitle_of_docid = {}
d_global = 0.85
adj_list = []
num_links = []
pagerank_values_old = []
pagerank_values = []

def convert_title(link):
    # Some links have a section for the page category, which is cut
    # here. The title is also converted to lowercase.
    div_pos = link.find('|')
    if div_pos != -1:
        return link.lower()[:div_pos]
    else:
        return link.lower()

with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)
doc_titles = set(map(convert_title, doc_titles))

def gather_sites():
    # list all documents that are actually linked to by some other
    # document
    for doc_no, doc in enumerate(load_wikidata(filename)):
        links = find_internal_links(doc["text"])
        for link in links:
            linktext = convert_title(link)
            if linktext in doc_titles:
                all_links.add(linktext)

def build_docid_mapping():
    # build a mapping document titles to integers to save space
    global num_docs
    for link in all_links:
        if link not in docid_of_doctitle:
            docid_of_doctitle[link] = num_docs
            doctitle_of_docid[num_docs] = link
            num_docs += 1

def build_adj_list():
    # build an adjacency list for the internal links of the dataset;
    # an edge from some node B to some node A exists iff A links to B
    global adj_list, num_links
    adj_list = [[] for i in range(num_docs)]
    # we also keep track of the number of outgoing links for each
    # document
    num_links = np.zeros(num_docs)
    done = set()
    for doc_no, doc in enumerate(load_wikidata(filename)):
        if convert_title(doc["title"]) not in all_links: continue
        own_title = convert_title(doc["title"])
        # if document already processed (for some reason there are
        # multiple copies of one document in some datasets), skip
        if (docid_of_doctitle[own_title] in done): continue
        # we only want to look at processable links
        links = set(map(convert_title, find_internal_links(doc["text"]))).intersection(all_links)
        num_links[docid_of_doctitle[own_title]] = len(links)
        for link in links:
            adj_list[docid_of_doctitle[link]].append(docid_of_doctitle[own_title])
        done.add(docid_of_doctitle[own_title])

def calc_pagerank_head():
    global pagerank_values, pagerank_values_old
    # initialize pagerank values
    initial_value = 1.0 / num_docs
    pagerank_values_old = [initial_value for i in range(num_docs)]
    pagerank_values = [0 for i in range(num_docs)]
    # apply pagerank update 100 times
    for i in range(100):
        update_pagerank_arr()

def update_pagerank_arr():
    global pagerank_values, pagerank_values_old
    # apply update for each node
    for i in range(num_docs):
        update_pagerank_value(i)
    # save the new pagerank values for DP in next iteration
    pagerank_values_old = pagerank_values


def update_pagerank_value(index):
    # update a single pagerank value
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

# map document titles to their respective pagerank values
pagerank_mapping = {}
for site in pagerank_final_values:
    pagerank_mapping[doctitle_of_docid[site[0]]] = site[1]

with open("pagerank.pickle", "wb") as f:
    pickle.dump(pagerank_mapping, f)
print("done")
