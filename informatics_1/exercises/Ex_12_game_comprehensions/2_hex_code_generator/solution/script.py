#!/usr/bin/env python3

import random

class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        """returns a list of n random 4-digit hex codes"""
        address_chars = "0123456789ABCDEF"
        n = self.columns * self.rows

        def c(): return random.choice(address_chars)

        addresses = [[c(), c(), c(), c()] for i in range(n)]
        return ["0x%s%s%s%s" % (a, b, c, d) for a, b, c, d in addresses]

