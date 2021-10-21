```python
python
counts = dict()
names = ['ab', 'cd', 'ef', 'gh', 'cd', 'gh', 'cd']
for name in names:
	counts[name] = counts.get(name, 0) + 1

names.sort()
```
- create a dict
- val is the number of occurrences of the key