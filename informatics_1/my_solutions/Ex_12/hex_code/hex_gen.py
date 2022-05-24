#!/usr/bin/env python3

from random import choice


class GameRunner(object):
    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        chars = "0123456789ABCDEF"

        def gen():
            for _ in range(self.columns * self.rows):
                code = "0x"
                for _ in range(4):
                    code += choice(chars)
                yield code

        return list(gen())
