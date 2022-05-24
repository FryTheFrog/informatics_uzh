import re

class ProfanityFilter:

    def __init__(self, keywords, template):
        self.keywords = sorted(keywords, key=len, reverse=True)
        self.__template = template

    def __clean(self, word):
        badword = False
        rest = ['', '']
        for i in self.keywords:
            if i.lower() in word.lower():
                rest = re.split(i, word, flags=re.IGNORECASE)
                badword = True
                break
            else: continue
        if badword:    
            factor = len(word) // len(self.__template) + 1
            clean = factor * self.__template
            clean = rest[0] + clean[:len(word)] + rest[1]
            return clean
        else: return word

    def filter(self, msg):
        for word in msg.split():
            msg = msg.replace(word, self.__clean(word))
        return msg

f = ProfanityFilter(["duck", "theduck" ,"Shot", "batch", "mastard"], "?#$")
offensive_msg = "theduck absHOtc DebATChfghi AaaMaStard jklMnoDUCK duck sHOt"
clean_msg = f.filter(offensive_msg)