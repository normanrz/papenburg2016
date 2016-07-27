from stemming.porter2 import stem
import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)

while True:
    search_token = stem(input("Query: ").strip().lower())
    results = [doc_titles[doc_no] for doc_no in index[search_token]]
    print(results)
    print(len(results))
