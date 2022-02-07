from collections import Counter

def count_letters(file):
    with open(file) as fp:
        text = fp.read().lower()
    return Counter(file)
