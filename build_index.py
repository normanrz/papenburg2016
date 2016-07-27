from load_dataset import load_wikidata, clean_wikidata
from preprocess import tokenize_and_stem
from collections import defaultdict
import pickle

index = defaultdict(list)

doc_titles = [doc["title"] for doc in load_wikidata("papenburg-datasets/dewiki-small.json")]

for i, doc in enumerate(load_wikidata("papenburg-datasets/dewiki-small.json")):
    tokens = tokenize_and_stem(clean_wikidata(doc["text"]))
    token_set = set(tokens)
    for token in token_set:
        index[token].append(i)

search_token = input("Query: ")
results = [doc_titles[doc_no] for doc_no in index[search_token]]
print(results)

with open("index.pickle", "wb") as f:
    pickle.dump(index, f)
with open("doc_titles.pickle", "wb") as f:
    pickle.dump(doc_titles, f)
