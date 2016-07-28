from preprocess import tokenize_and_stem
import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)

while True:
    search_tokens = tokenize_and_stem(input("Query: "))
    all_results = []
    for i, token in enumerate(search_tokens):
        if i == 0:
            all_results = index[token]
        else:
            all_results = [doc_no for doc_no in index[token] if doc_no in all_results]

    print([doc_titles[doc_no] for doc_no in all_results])
    print(len(all_results))
