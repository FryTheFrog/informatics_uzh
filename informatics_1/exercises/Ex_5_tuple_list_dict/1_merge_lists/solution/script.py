#!/usr/bin/env python3

def merge(a ,b):

    if len(a) == 0 or len(b) == 0:
        return []

    maxlen = max(len(a), len(b))

    cur_a = None
    cur_b = None
    res = []

    for i in range(maxlen):
        if i < len(a):
            cur_a = a[i]
        if i < len(b):
            cur_b = b[i]
        res.append((cur_a, cur_b))

    return res
