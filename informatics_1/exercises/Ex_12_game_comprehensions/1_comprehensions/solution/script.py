#!/usr/bin/python3

from public.data import words

def words_with_length(length):
    return [word for word in words if len(word) == length]

def words_containing_string(s):
    return [word for word in words if s in word]

def words_starting_with_character(c):
    return [word for word in words if word.startswith(c)]

def alphabet():
    import string
    return string.ascii_lowercase

def dictionary():
    return {c: words_starting_with_character(c) for c in alphabet()}

def censored_words(s):
    return [word if s not in word else "x" * len(word) for word in words]

