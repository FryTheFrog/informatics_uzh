```python
def tri_recursion(k):
	if(k > 0):
		result = k + tri_recursion(k - 1)
		print(result)
	else:
		result = 0
	return result
```


```python
def gcd(a, b):
    a, b = absolute_value(a), absolute_value(b)
    if a == 0 and b == 0:
        return None
    if b == 0:
        return a
    return gcd(b, a % b)
```
- finds the greatest common divisor using ‘euclidian algorithm’