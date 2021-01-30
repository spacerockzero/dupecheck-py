from lib import functions
from tests import generated as mocks
import os
import numpy as np

# copy test dataset file to string
filepath=os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'dataset.txt'))
with open(filepath,'r') as fin:
  dataset = fin.read()

# test the functions

def test_make_chunks():
  lst = ['a','b','c','d']
  expected = [['a','b'],['c','d']]
  chunked = functions.make_chunks(lst, 2)
  np.array_equal(np.array(chunked), np.array(expected))

def test_chunkit():
  str = 'I know chicken math'
  expected = [['I','know'],['chicken','math']]
  chunked = functions.chunkit(str, 2)
  np.array_equal(np.array(chunked), np.array(expected))

def test_unique():
  duplicates = functions.run(3, mocks.unique, dataset)
  assert(len(duplicates) == 0)

def test_series3():
  duplicates = functions.run(3, mocks.duplicate_series3, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series3_common)

def test_series4():
  duplicates = functions.run(4, mocks.duplicate_series4, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series4_common)

def test_series5():
  duplicates = functions.run(5, mocks.duplicate_series5, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series5_common)

def test_series6():
  duplicates = functions.run(6, mocks.duplicate_series6, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series6_common)
