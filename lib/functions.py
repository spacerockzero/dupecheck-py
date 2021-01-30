# TODO: use sliding windows instead of chunking.
# the chunking method fails when part of a dupe string
# crosses the border between chunks

import colorama
from colorama import Fore
import tqdm

colorama.init(autoreset=True)

DEFAULT_MIN = 5
DEFAULT_MAX = 10

def striplist(l):
  # clean out some unneeded chars
	return([x.strip(' \t\n\r') for x in l])

def compare(input):
  # main comparison function
	test = input[0]
	data = input[1]
	found = data.find(test)
	if found != -1:
		return test

def make_chunks(lst, n):
	# Yield successive n-sized chunks from lst.
	for i in range(0, len(lst), n):
		yield lst[i:i + n]

def chunkit(str, chunk_length):
  # make chunks of strings the way we like
	chunks=[]
	list = str.split()
	list = striplist(list)
	wordLists = make_chunks(list, chunk_length)
	for chunk in wordLists:
		if chunk != '':
			chunk = ' '.join(chunk)
			chunks.append(chunk)
	return chunks

def run(chunk_length, text, dataset):
  print('chunk_length, text, dataset',chunk_length, text, dataset)
  testChunks = chunkit(text, chunk_length)
  # remove empty lines
  testChunks = list(filter(None, testChunks))
  results = []
  for testLine in testChunks:
    found = compare([testLine, dataset])
    # print('found', found)
    if found != None:
      results.append(found)
  return results

def copycheck(min=DEFAULT_MIN, max=DEFAULT_MAX, text=None, dataset=None, verbose=False):
  assert(text != None)
  assert(dataset != None)
  matches = []
  for i in tqdm(range(max, min, -1)):
    res = run(i, dataset)
    if len(res) > 0:
      matches.append([i, res])
  return matches
