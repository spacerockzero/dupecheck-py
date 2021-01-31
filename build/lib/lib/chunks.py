# TODO: use sliding windows instead of chunking.
# the chunking method fails when part of a dupe string
# crosses the border between chunks

import colorama
from colorama import Fore
from tqdm import trange, tqdm
import os

colorama.init(autoreset=True)

DEFAULT_MIN = 5
DEFAULT_MAX = 10


def striplist(l):
    # clean out some unneeded chars
    return [x.strip(" \t\n\r") for x in l]


def compare(input):
    # main comparison function
    test = input[0]
    data = input[1]
    chunk_length = input[2]
    # print("data", data)
    found = data.find(test)
    if found != -1:
        words = test.split()
        # don't return matched chunks shorter than the current chunk
        # length, even if they are rounding remainder orphans from the
        # chunking process
        if len(words) >= chunk_length:
            return test


def make_chunks(lst, n):
    # Yield successive n-sized chunks from lst.
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def chunkit(str, chunk_length):
    # make chunks of strings the way we like
    chunks = []
    list = str.split()
    list = striplist(list)
    wordLists = make_chunks(list, chunk_length)
    for chunk in wordLists:
        if chunk != "":
            chunk = " ".join(chunk)
            chunks.append(chunk)
    return chunks


def run(chunk_length, text, dataset):
    dataset = dataset.replace(os.linesep, " ")
    testChunks = chunkit(text, chunk_length)
    # remove empty lines
    testChunks = list(filter(None, testChunks))
    results = []
    for testLine in testChunks:
        found = compare([testLine, dataset, chunk_length])
        if found != None:
            print("found", found)
            results.append(found)
    return results


def dupecheck(min=DEFAULT_MIN, max=DEFAULT_MAX, text=None, dataset=None, verbose=False):
    assert text != None
    assert dataset != None
    text = text.replace(os.linesep, "")
    matches = []
    for i in trange(max, min, -1):
        # print('text, i',text, i)
        res = run(i, text, dataset)
        if len(res) > 0:
            for r in res:
                if r not in matches:
                    matches.append(r)
    return matches
