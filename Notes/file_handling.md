```python
with open(path_r, 'r') as in_file, open(path_w, 'w') as out_file:
```
- easiest way to read from a file and write into a new one at the same time
- in\_file and out\_file can be referenced as normal vars

**not necessary**
```python
in_file.close()
out_file.close()
```
- files should usually be closed if no longer needed
- using the *with* statement the files close automatically after block is finished