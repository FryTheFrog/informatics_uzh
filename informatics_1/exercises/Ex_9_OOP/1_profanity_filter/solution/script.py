#!/usr/bin/env python3

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.__keywords = []
        for kw in keywords:
            self.__keywords.append(kw.lower())
        self.__keywords = reversed(sorted(self.__keywords))
        self.__template = template

    def filter(self, msg):
        msg_lower = msg.lower()
        for word in self.__keywords:
            while word in msg_lower:
                idx = msg_lower.find(word)
                msg = self.__replace(msg, idx, word)
                msg_lower = self.__replace(msg_lower, idx, word)
        return msg

    def __replace(self, s, idx, word):
        clean_word = self.__escape(word)
        return s[:idx] + clean_word + s[idx+len(clean_word):]

    def __escape(self, word):
        res = ""
        for idx, _ in enumerate(word):
            t_idx = idx % len(self.__template)
            res += self.__template[t_idx]
        return res
