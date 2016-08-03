from load_dataset import load_wikidata, clean_wikidata
from preprocess import tokenize_and_stem, count_tokens, max_count_token
from collections import defaultdict
from os import path
import pickle

filename = path.join("datasets", "pokemon.json.gz")
index = defaultdict(dict)

doc_titles = [doc["title"] for doc in load_wikidata(filename)]

for doc_no, doc in enumerate(load_wikidata(filename)):
    tokens = tokenize_and_stem(clean_wikidata(doc["text"]))
    if len(tokens) == 0:
        continue
    token_counts = count_tokens(tokens)
    max_token_count = max_count_token(token_counts)
    token_set = token_counts.keys()
    for token in token_set:
        tf = token_counts[token] / max_token_count
        index[token][doc_no] = tf

with open("index.pickle", "wb") as f:
    pickle.dump(index, f)
with open("doc_titles.pickle", "wb") as f:
    pickle.dump(doc_titles, f)
