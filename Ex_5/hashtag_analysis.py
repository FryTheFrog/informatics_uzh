posts = [
    "hi #weekend",
    "good morning #zurich #limmat",
    "spend my #weekend in #zurich",
    ".#zurich <3",
    "#123",
    "#",
    "#ZURICH.BERN",
    "asdf #a asdf",
    "##a"
    ]
# analyze() should return: {weekend: 2, zurich: 3, limmat: 1, ZURICH: 1, a: 2}

def analyze(posts):
    #takes iterable, returns gen with elems in list, that include '#'
    def hashtag_finder(list):
        for i in list:
            if '#' in i:
                yield i

    #takes str, returns str with everything after 1st '#'
    def cut_front(str):
        return str[str.find('#'):]
    cut_posts = map(cut_front, hashtag_finder(posts)) #generator -> map

    #takes str, returns str, splits at '#', !adds empty hashtags!
    def split_tags(str):
        str = str.split('#')
        return str
    split_posts = map(split_tags, cut_posts) # map -> map containing lists
    split_posts = [item for sublist in split_posts for item in sublist] # nested list -> flat list

    #takes str, returns str, removes 1st char that isnt alnum and everything after
    def cut_back(str):
        clean_str = ''
        for i in str:
            if i.isalnum():
                clean_str += i
            else:
                break
        return clean_str
    cut_split_posts = map(cut_back, split_posts) # list -> map

    #takes iterable, returns gen with valid hashtags
    def del_invalid(list):
        for i in list:
            if i != '' and i[0].isalpha():
                yield i
    hashtags_list = del_invalid(cut_split_posts) # map -> generator

    hashtags_dict ={}
    for i in hashtags_list: #counts hashtag occurences
        hashtags_dict[i] = hashtags_dict.get(i, 0) + 1

    return hashtags_dict                    

print(analyze(posts))