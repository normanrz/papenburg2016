from preprocess import tokenize_and_stem
import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)

while True:
    search_tokens = tokenize_and_stem(input("Query: "))

    # Perform OR query
    all_docs = []
    for i, token in enumerate(search_tokens):
        all_docs += index[token]
    all_docs = set(all_docs)

    # Calculate dot products
    dot_docs = {}
    for doc_no in all_docs:
        # dot = sum([index[token].count(doc_no) for token in search_tokens])
        dot = 0
        for token in search_tokens:
            dot += index[token].count(doc_no)
        dot_docs[doc_no] = dot

    # Sort by dot product
    ranked_docs = sorted(dot_docs, key=dot_docs.get, reverse=True)

    print([doc_titles[doc_no] for doc_no in ranked_docs])
    print(len(ranked_docs))
