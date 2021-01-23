from lib import functions
from tests import generated as mocks
import os

filepath=os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'dataset.txt'))
with open(filepath,'r') as fin:
  dataset = fin.read()

def test_unique():
  duplicates = functions.copycheck(3, mocks.unique, dataset)
  assert(len(duplicates) == 0)

def test_series3():
  duplicates = functions.copycheck(3, mocks.duplicate_series3, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series3_common)

def test_series4():
  duplicates = functions.copycheck(4, mocks.duplicate_series4, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series4_common)

def test_series5():
  duplicates = functions.copycheck(5, mocks.duplicate_series5, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series5_common)

def test_series6():
  duplicates = functions.copycheck(6, mocks.duplicate_series6, dataset)
  assert(len(duplicates) == 1)
  assert(duplicates[0] == mocks.duplicate_series6_common)
