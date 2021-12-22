# Dataset contains data that will be reverse indexed
dataset = [
    "Hello world",
    "This is the WORLD",
    "hello again"
 ] 

def reverse_index(dataset):

    index_dictionary = {} 

    # Loop through dataset
    for index,current_data in enumerate(dataset) :
        # Split current_data to find words
        word_list = current_data.split()
        # Loop through wordList 
        for current_word in word_list:
            # Make the word case insensitive by converting it to lowercase
            current_word = current_word.lower()
            # Append the index of the word to the dictionary
            if current_word not in index_dictionary:
                index_dictionary[current_word] = []
            index_dictionary[current_word].append(index)

    return index_dictionary

print(reverse_index(dataset))
