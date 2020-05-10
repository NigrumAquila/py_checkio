from string import punctuation
remove_punctuation = str.maketrans('', '', punctuation)

def fitness(w1, w2):
    sw1, sw2 = set(w1), set(w2)
    return sum((10 * (w1[0] == w2[0]),
                10 * (w1[-1] == w2[-1]),
                30 * (min(len(w1), len(w2)) / max(len(w1), len(w2))),
                50 * (len(sw1 & sw2) / len(sw1 | sw2))))
    

def find_word(sentence):
    words = sentence.lower().translate(remove_punctuation).split()[::-1]
    return max(words, key = lambda w: sum(fitness(w, x) for x in words)) 