"""Generate Markov text from text files."""

#from random import choice
import random 


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    read_file = open(file_path).read()

    return read_file


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """
    list_of_words = text_string.split()
    chains = {}
    for i in range(len(list_of_words)-2):
        key = (list_of_words[i], list_of_words[i+1]) #Create keys as tuple
        value = (list_of_words[i+2])
        if key not in chains:
            chains[key] = []
        chains[key].append(value)
    
    # for i in range(len(list_of_words)-2):
    #     for bigram,value in chains.items():
    #         if bigram == (list_of_words[i], list_of_words[i+1]):
    #             bigram = value.append(list_of_words[i+2])
    #print(chains)
    return chains


def make_text(chains):
    """Return text from chains."""
    
    #While True:
    #pick a randomly selected key using random.choice from the dictionary
    #append to words[]
    #from values of this key, use random.choice to pick a random value from the list "value"
    #append it to words[]
    #assign (key[1], value) to the next iteration of text generation and proceed
    words = []
    new_key = random.choice(list(chains))
    words.extend(new_key) #splits the tuple up and adds each element individually
    new_value = random.choice(list(chains[new_key]))
    words.append(new_value)

    while True:
        new_key = (words[-2],words[-1])
        if new_key in chains:
            new_value = random.choice(list(chains[new_key]))
            words.append(new_value)
        else:
            break
        
    # your code goes here
    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
