from load_dataset import load_wikidata, clean_wikidata
from preprocess import tokenize_and_stem
from collections import defaultdict
from os import path
import pickle

filename = path.join("datasets", "pokemon_pages_current.json.gz")
index = defaultdict(list)

doc_titles = [doc["title"] for doc in load_wikidata(filename)]

for i, doc in enumerate(load_wikidata(filename)):
    tokens = tokenize_and_stem(clean_wikidata(doc["text"]))
    token_set = set(tokens)
    for token in token_set:
        index[token].append(i)

with open("index.pickle", "wb") as f:
    pickle.dump(index, f)
with open("doc_titles.pickle", "wb") as f:
    pickle.dump(doc_titles, f)
