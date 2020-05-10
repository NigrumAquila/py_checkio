VOWELS = "AEIOUYaeiouy"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZbcdfghjklmnpqrstvwxz"

def checkio(text):
    counter = 0
    text = text.replace(",", " ").replace(".", " ").replace(";", " ").replace("?", " ")
    text = text.split(" ")
    for word in text:
        pomoc = 0
        for letter in range(len(word) - 1):
            if word[letter] in VOWELS and word[letter + 1] in CONSONANTS:
                pomoc += 1
            elif word[letter] in CONSONANTS and word[letter + 1] in VOWELS:
                pomoc += 1
        if len(word) != 1:
            if pomoc == (len(word) - 1):
                counter += 1
    return counter