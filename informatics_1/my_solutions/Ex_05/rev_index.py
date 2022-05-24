dataset = [
    "Hello world world",
    "This is the WORLD",
    "hello again",
    "what the fuck is this",
    "what the fuck is that",
    "why does it not work",
    "fuck this shit i am out",
    "hello shit world",
    "fuck this world",
    "why am i",
    "it is shit",
    "hello that shit",
]


def reverse_index(dataset):
    index_dict = {}
    for idx, str in enumerate(dataset):
        words = str.lower().split()
        for word in words:
            if word in index_dict:
                index_dict[word].append(idx)
            else:
                index_dict[word] = [idx]
    return index_dict


print(reverse_index(dataset))
