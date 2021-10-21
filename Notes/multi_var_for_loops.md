```python
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
]

def reverse_index(dataset):
    index_dict = {}
    for idx, str in enumerate(dataset): #multi var, multi iterables
        words = str.lower().split()
        for word in words:
            if word in index_dict:
                index_dict[word].append(idx)
            else: index_dict[word] = [idx]
    return index_dict
```

- for loop iterates through two iterables at the same time
- enumerate() returns an obj with two expr
	- ex. (1, ‘Hello world’)
- idx iterates though indexes, str iterates though strings

* creates a dict with words as keys and list of indices as val