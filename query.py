from preprocess import tokenize_and_stem
import math
import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)

N = len(doc_titles)

while True:
    search_tokens = tokenize_and_stem(input("Query: "))

    # Perform OR query
    all_docs = []
    for i, token in enumerate(search_tokens):
        all_docs += index[token]
    all_docs = set(all_docs)

    # Calculate tfidf scores
    doc_scores = {}
    idf_values = {token: math.log(N / len(index[token])) for token in search_tokens}
    for doc_no in all_docs:
        score = 0
        for token in search_tokens:
            if doc_no in index[token]:
                tf = index[token][doc_no]
                idf = idf_values[token]
                score += tf * idf
        doc_scores[doc_no] = score

    # Sort by tfidf scores
    ranked_docs = sorted(doc_scores, key=doc_scores.get, reverse=True)

    print([doc_titles[doc_no] for doc_no in ranked_docs])
    print(len(ranked_docs))
