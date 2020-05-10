def cards(deck, hand):
    last = -1
    for n in sorted(hand):
        if last == n:
            return False
        last = n - (n - last != 1)
    return last < deck