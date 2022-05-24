#!/usr/bin/python3

from data import words
from string import ascii_lowercase


def words_with_length(length):
    return [word for word in words if len(word) == length]


def words_containing_string(s):
    return [word for word in words if s in word]


def words_starting_with_character(c):
    return [word for word in words if c == word[0]]


def alphabet():
    """you don't have to solve this one using a comprehension."""
    return ascii_lowercase


def dictionary():
    return {
        k: v
        for k, v in zip(
            alphabet(), [words_starting_with_character(i) for i in alphabet()]
        )
    }


def censored_words(s):
    return [len(word) * "x" if s in word else word for word in words]
