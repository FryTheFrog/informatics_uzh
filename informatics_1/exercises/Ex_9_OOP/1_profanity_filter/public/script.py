#!/usr/bin/env python3

class ProfanityFilter:
    def __init__(self, keywords, template):
        pass

    def __clean(self, word):
        pass

    def filter(self, msg):
        pass

# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    f = ProfanityFilter(["duck", "shot", "batch", "mastard"], "?#$")
    offensive_msg = "abc defghi mastard jklmno"
    clean_msg = f.filter(offensive_msg)
    print(clean_msg)  # abc defghi ?#$?#$? jklmno
