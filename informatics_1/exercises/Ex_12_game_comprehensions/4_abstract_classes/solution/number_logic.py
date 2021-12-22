#!/usr/bin/env python3

from random import choice
from public.game_logic import GameLogic

class NumberLogic(GameLogic):

    def check(self, guess):
        if len(guess) != len(self.password):
            raise Warning("Number of digits is different from the password")
        for i in range(0, 10):
            if guess.count(str(i)) > 1:
                raise Warning("Guess contains repeated number")
        return super().check(guess)

    def _word_selection(self):
        words = []
        number_chars = "0123456789"

        def c():
            return choice(number_chars)

        for i in range(self.num_words):
            word = []
            for j in range(self.len_words):
                next = None
                while next is None:
                    cand = c()
                    if cand not in word:
                        next = cand
                word.append(next)
            words.append("".join(word))

        return words

    def _generate_feedback(self, guess):
        num_contained = 0
        for i in guess:
            if i in self.password:
                num_contained += 1
        self.num_attempts -= 1
        return "{}/{} correct".format(num_contained, self.len_words)
