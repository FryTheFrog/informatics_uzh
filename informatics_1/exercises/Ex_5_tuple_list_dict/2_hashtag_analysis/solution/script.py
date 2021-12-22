#!/usr/bin/env python3

def analyze(posts):
    tags = {}

    for post in posts:
        curHashtag = None
        for c in post:
            is_allowed_char = c.isalnum()

            if curHashtag != None and not is_allowed_char:
                if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                    if curHashtag in tags.keys():
                        tags[curHashtag] += 1
                    else:
                        tags[curHashtag] = 1
                curHashtag = None

            if c == "#":
                curHashtag = ""
                continue

            if c.isalnum() and curHashtag != None:
                curHashtag += c

        if curHashtag != None:
            if len(curHashtag) > 0 and not curHashtag[0].isdigit():
                if curHashtag in tags.keys():
                    tags[curHashtag] += 1
                else:
                    tags[curHashtag] = 1

    return tags
