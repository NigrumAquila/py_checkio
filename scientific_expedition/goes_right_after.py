def goes_after(word: str, first: str, second: str) -> bool:
    return ''.join(sorted(set(word), key=word.index)).find(first+second) != -1