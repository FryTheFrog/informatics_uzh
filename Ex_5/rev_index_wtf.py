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
    "hello that shit"
 ] 

def reverse_index(dataset):
    index_dictionary = {}
    nested_dataset = []
    for str in dataset: #creates a nested list, sublist countains single words of str
        str = str.split()
        nested_dataset.append(str)
        for key in str: #using words in sublist as keys, create dict
            key = key.lower()
            index_dictionary[key] = index_dictionary.get(key, []) + [nested_dataset.index(str)]
    for key in index_dictionary: #remove duplicates from val lists
        index_dictionary[key] = list(dict.fromkeys(index_dictionary[key]))
    return index_dictionary

print(reverse_index(dataset))