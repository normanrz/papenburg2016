import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)

while True:
    search_token = input("Query: ")
    results = [doc_titles[doc_no] for doc_no in index[search_token]]
    print(results)
    print(len(results))
