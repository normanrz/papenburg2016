import re
from stemming.porter2 import stem
from nltk.stem.snowball import GermanStemmer
from collections import defaultdict
import unicodedata

tokenize_re = re.compile("\w{2,}")
digits_only_re = re.compile("^\d+$")


def tokenize(text):
    tokens = [token.lower() for token in tokenize_re.findall(text)]
    # tokens_without_numbers = ["number" if digits_only_re.match(token) else token for token in tokens]
    return tokens


def tokenize_and_stem(text):
    return [stem(clean_token(token)) for token in tokenize(text)]


def tokenize_and_stem_german(text):
    stemmer = GermanStemmer()
    return [clean_token(stemmer.stem(token)) for token in tokenize(text)]


def clean_token(token):
    return ''.join(c for c in unicodedata.normalize('NFD', token) if unicodedata.category(c) != 'Mn')


def count_tokens(tokens):
    counter = defaultdict(int)
    for token in tokens:
        counter[token] += 1
    return counter


def max_count_token(token_counts):
    return token_counts[max(token_counts, key=token_counts.get)]
