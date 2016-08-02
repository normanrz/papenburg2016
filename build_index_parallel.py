from load_dataset import load_wikidata, clean_wikidata
from preprocess import tokenize_and_stem, count_tokens, max_count_token
from collections import defaultdict
from multiprocessing import Pool, cpu_count
from os import path
import pickle

filename = path.join("datasets", "pokemon.json.gz")


def process_doc_titles():
    docs = load_wikidata(filename)
    doc_titles = [doc["title"] for doc in docs]
    print("Read {} doc titles".format(len(doc_titles)))
    with open("doc_titles.pickle", "wb") as f:
        pickle.dump(doc_titles, f)


def process_doc_texts():
    pool = Pool(cpu_count())
    docs = load_wikidata(filename)
    doc_texts = (clean_wikidata(doc["text"]) for doc in docs)
    doc_tokens = pool.imap(tokenize_and_stem, doc_texts)
    doc_tokens = (set(tokens) for tokens in doc_tokens)

    index = defaultdict(dict)
    for doc_no, tokens in enumerate(doc_tokens):
        if len(tokens) == 0:
            continue
        token_counts = count_tokens(tokens)
        max_token_count = max_count_token(token_counts)
        token_set = token_counts.keys()
        for token in token_set:
            tf = token_counts[token] / max_token_count
            index[token][doc_no] = tf

        if doc_no % 1000 == 0:
            print("Indexed {} documents".format(doc_no))
    print("Done indexing")

    with open("index.pickle", "wb") as f:
        pickle.dump(index, f)


process_doc_titles()
process_doc_texts()
