from load_dataset import load_wikidata, clean_wikidata
from preprocess import tokenize_and_stem
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from os import path
import pickle

pool = Pool(cpu_count())

docs = list(load_wikidata(path.join("datasets", "pokemon_pages_current.json.gz")))
print("Found {} documents".format(len(docs)))
doc_titles = [doc["title"] for doc in docs]

doc_texts = [clean_wikidata(doc["text"]) for doc in docs]
doc_tokens = list(pool.map(tokenize_and_stem, doc_texts))
doc_tokens = [set(tokens) for tokens in doc_tokens]
print("Done preprocessing")

index = defaultdict(list)
for i, tokens in enumerate(doc_tokens):
    for token in tokens:
        index[token].append(i)
print("Done indexing")

with open("index.pickle", "wb") as f:
    pickle.dump(index, f)
with open("doc_titles.pickle", "wb") as f:
    pickle.dump(doc_titles, f)
