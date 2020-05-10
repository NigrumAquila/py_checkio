VOWELS = "aeiouy"

def translate(phrase):
    human_phrase = []
    i = 0

    while i < len(phrase):
        human_phrase.append(phrase[i])
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    return ''.join(human_phrase)