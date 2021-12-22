#!/usr/bin/env python3

import random
from difflib import SequenceMatcher
from math import floor
from random import shuffle, choice


class WordLogic(object):

    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)

        num_random = floor(self.num_words / 3)
        selected_words = words[:num_random]
        remaining_words = words[num_random:]

        while len(selected_words) < self.num_words:
            existing = choice(selected_words)
            found = False
            while not found:
                candid = choice(remaining_words)
                if candid not in selected_words and self.is_similar(existing, candid, 0.4):
                    selected_words.append(candid)
                    found = True

        return selected_words

    def is_similar(self, a, b, threshold):
        sim = SequenceMatcher(None, a, b).ratio()
        return sim > threshold
