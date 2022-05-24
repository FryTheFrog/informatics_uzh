#!/usr/bin/env python3

import random
from difflib import SequenceMatcher
from math import floor


class WordLogic(object):
    def __init__(self, num_words, len_words):
        self.num_words = num_words
        self.len_words = len_words

    def find_words_with_right_size(self):
        with open("resource/words.txt") as f:
            word_list = f.read().splitlines()
        return [word.upper() for word in word_list if len(word) is self.len_words]

    def is_similar(self, a, b, threshold):
        if SequenceMatcher(None, a, b).ratio() > threshold:
            return True
        else:
            return False

    def word_selection(self):
        words = self.find_words_with_right_size()
        random.shuffle(words)
        num_pool = floor(self.num_words / 3)
        selected_word = random.choice(words[:num_pool])
        words_pool = words[num_pool:]
        res = [selected_word]
        while len(res) < self.num_words:
            temp = random.choice(words_pool)
            if temp not in res and self.is_similar(selected_word, temp, 0.4):
                res.append(temp)
        return res
