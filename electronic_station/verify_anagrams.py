import string

def verify_anagrams(first_word, second_word):
    to_list = lambda y: sorted(map(lambda x: x.lower(), filter(lambda x: x.lower() in string.ascii_lowercase, y)))
    return to_list(first_word) == to_list(second_word)