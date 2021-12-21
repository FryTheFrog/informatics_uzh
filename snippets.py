# LISTS
# clone a list (list must be flat)
def clone_list(lst) -> list:
    return lst[:]

# clone a nested list (2D) 
def clone_nested_list(lst) -> list:
    return [[item for item in sub_list] for sub_list in lst]

# clone a nested list (N-Dimensional)
def deep_copy(lst) -> list:
    if type(lst) is list:
        return [deep_copy(item) for item in lst]
    else:
        return lst

# find elem with most occurence
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# check for duplicates
def all_unique(lst) -> bool:
    return len(lst) == len(set(lst))

# chunk list into smaller lists
def chunk_list(lst, size) -> list:
    return [lst[i:i+size] for i in range(0, len(lst), size)]

# deep flatten a nested list
def deep_flatten(lst) -> list:
    flat_list = []
    [flat_list.extend(deep_flatten(i)) for i in lst] if isinstance(lst, list) else flat_list.append(lst)
    return flat_list

# all val combinations from two lists
def combine_lists(lst1, lst2) -> list:
    return [(a, b) for a in lst1 for b in lst2]

# sum vals with the same idx from 2 lists
def sum_elems(lst1, lst2) -> list:
    return [a + b for a, b in zip(lst1, lst2)]

# DICTS
# sum of values
def dict_sum(d):
    vals = []
    for i in d:
        vals.append(d[i])
    return sum(vals)

# merge 2 dicts
def merge_dicts(d1, d2):
    merged = d1 | d2
    return merged

# advanced merge (combines vals to list)
from collections import defaultdict

def combine_values(*dicts) -> dict:
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)

# invert dict
def invert_dictionary(d) -> dict:
  return {value: key for key, value in d.items()}

# CSV
# parse a csv (dict for each line, header vals as keys)
import csv

def parse_csv(path:str) -> list:
    with open(path) as my_data:
        return list(csv.DictReader(my_data))

