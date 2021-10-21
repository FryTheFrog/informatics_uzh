```python
#doesn't work
nested_list = [['ab', 'cd'], 'ef', ['gh', 'cd', 'gh']]

#works
nested_list = [['ab', 'cd'], ['ef'], ['gh', 'cd', 'gh']]

flat_list = [item for sublist in nested_list for item in sublist]
```

- flattens a list containing lists
- only works if all elems in list are lists