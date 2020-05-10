from itertools import zip_longest


def checkio(text, word):
    horizontal = text.lower().replace(' ', '').splitlines()
    for i, row in enumerate(horizontal, 1):
        index = row.find(word)
        if index >= 0:
            return [i, index+1, i, index+len(word)]

    vertical = [''.join(line) for line in zip_longest(*horizontal, fillvalue='-')]
    for i, col in enumerate(vertical, 1):
        index = col.find(word)
        if index >= 0:
            return [index+1, i, index+len(word), i]