MAX_STR = 10  # max symbols in Braille's line
H, W = 3, 2   # height and width of Braille character

# create Braille alphabet
pattern = ['1010111110111110010110101111101111100101101011111001000000000000000001',
           '0010000101101111101100100001011011111011001000010111001011111000110001',
           '0000000000000000000010101010101010101010111111111111000001001111100111']
letters = [[pattern[i][j:j+W] for i in range(H)] for j in range(0, len(pattern[0]), W)]
BRAILLE = dict(zip('abcdefghijklmnopqrstuvxyzw ,.-?_!^#', letters))
BRAILLE.update(dict(zip('1234567890', letters)))

# formatting marks: '#' for number, '^' for capital
prefix = lambda ch: '#' if ch.isdigit() else '^' if ch.isupper() else ''

def braille_page(text_in: str):
    # prepare text before converting to Braille
    text_out = ''.join(prefix(char) + char.lower() for char in text_in)
    text_out = [text_out[i:i+MAX_STR] for i in range(0, len(text_out), MAX_STR)]
    text_out[-1] += ' ' * (len(text_out[0]) - len(text_out[-1]))

    # format Braille output
    braille_out = []
    for s in text_out:
        for i in range(H):
            braille_out.append('0'.join(BRAILLE[char][i] for char in s))
        braille_out.append('0' * len(braille_out[0]))
    braille_out = braille_out[:-1]
    return tuple((tuple(map(int, line)) for line in braille_out))