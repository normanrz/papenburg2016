import re
from stemming.porter2 import stem
from collections import defaultdict

tokenize_re = re.compile("\w{2,}")
digits_only_re = re.compile("^\d+$")


def tokenize(text):
    tokens = [token.lower() for token in tokenize_re.findall(text)]
    # tokens_without_numbers = ["number" if digits_only_re.match(token) else token for token in tokens]
    return tokens


def tokenize_and_stem(text):
    return [stem(token) for token in tokenize(text)]


def count_tokens(tokens):
    counter = defaultdict(int)
    for token in tokens:
        counter[token] += 1
    return counter
