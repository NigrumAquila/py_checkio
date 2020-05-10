from itertools import chain, combinations

def generate_spectrum_functions(lines):
    oneline = list(chain(*lines))
    yield lambda e: oneline.count(e)
    yield lambda e: [column.count(e) for column in zip(*lines)]
    yield lambda e: sorted([e == q for q in line] for line in lines)

def chain_from_sorted(lines):
    elements = set(chain(*lines))
    for get_spectrum in generate_spectrum_functions(lines):
        spectra = {e: get_spectrum(e) for e in elements}
        linespectra = [[spectra[e] for e in line] for line in lines]
        if all(s != t for s, t in combinations(linespectra, 2)):
            break

    iterspectra = iter(linespectra)
    return chain(*sorted(lines, key = lambda line: next(iterspectra)))

def checkio(crossword, words):
    numberlines = list(chain(crossword[::2], list(zip(*crossword))[::2]))
    table = dict(zip(*map(chain_from_sorted, (numberlines, words))))
    return [[table.get(number, ' ') for number in row] for row in crossword]