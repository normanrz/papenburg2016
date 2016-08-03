from preprocess import tokenize_and_stem
from pagerank import convert_title
from collections import defaultdict
import math
import pickle

with open("index.pickle", "rb") as f:
    index = pickle.load(f)
with open("doc_titles.pickle", "rb") as f:
    doc_titles = pickle.load(f)
with open("pagerank.pickle", "rb") as f:
    pagerank_mapping = pickle.load(f)
pagerank_mapping = defaultdict(int, pagerank_mapping)

N = len(doc_titles)

if __name__ == "__main__":
    while True:
        search_tokens = tokenize_and_stem(input("Query: "))

        # Perform OR query
        all_docs = []
        for i, token in enumerate(search_tokens):
            all_docs += index[token]
        all_docs = set(all_docs)

        # Calculate tfidf scores
        doc_scores = {}
        idf_values = {}
        for token in search_tokens:
            if len(index[token]) == 0: continue
            idf_values[token] = math.log(N / len(index[token]))
        for doc_no in all_docs:
            score = 0
            for token in search_tokens:
                if doc_no in index[token]:
                    tf = index[token][doc_no]
                    idf = idf_values[token]
                    score += tf * idf
            doc_scores[doc_no] = score

        # apply pagerank values
        ranked_docs = []
        for item in doc_scores.items():
            ranked_docs.append((doc_titles[item[0]],
                                pagerank_mapping[convert_title(doc_titles[item[0]])] * item[1]))

        # Sort by (tfidf * pagerank)
        ranked_docs = sorted(ranked_docs, key=lambda x:x[1], reverse=True)

        print("## Found {} documents. Most relevant titles: ##".format(len(ranked_docs)))
        for doc in ranked_docs[0:30]:
            print(doc[0])
