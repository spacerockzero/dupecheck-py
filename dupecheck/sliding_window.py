# Use sliding windows instead of chunking.
# the chunking method fails when part of a dupe string
# crosses the border between chunks
import os
import re
from tqdm import trange, tqdm

DEFAULT_MIN = 5
DEFAULT_MAX = 10


def clean_string(s):
    s = s.replace(os.linesep, " ")
    s = re.sub(r"[^\w\s]", "", s)
    s = s.strip()
    return s


def compare(text, data):
    text = clean_string(text)
    found = data.find(text)
    if found != -1:
        return text


def run(window_length, text, dataset):
    print("window: " + str(window_length))
    dataset = clean_string(dataset)
    results = []
    text_words = text.split()
    for num, t_word in tqdm(iterable=enumerate(text_words), total=len(text_words)):
        window_indexes = list(range(num, num + window_length))
        window_words = ""
        for i in window_indexes:
            if i < len(text_words):
                word = text_words[i]
                if word != None:
                    window_words += word + " "
        duplicate_text = compare(window_words, dataset)
        if duplicate_text != None:
            wrds = duplicate_text.split()
            if len(wrds) >= window_length:
                results.append(duplicate_text)
    return results


def dupecheck(min=DEFAULT_MIN, max=DEFAULT_MAX, text=None, dataset=None, verbose=False):
    assert text != None
    assert dataset != None
    min = min - 1
    dataset = clean_string(dataset)
    matches = set([])
    for i in range(max, min, -1):
        res = run(i, text, dataset)
        if len(res) > 0:
            matches.update(res)
    matchs = sorted(matches, key=len)
    return matches
