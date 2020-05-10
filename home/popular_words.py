import re

def popular_words(text: str, words: list) -> dict:
    d = dict();
    print(text)
    text = re.sub('\n', ' ', text);
    for idx, word in enumerate(words):
        count = len(re.findall(r"\b(?=\w)" + re.escape(words[idx]) + r"\b(?!\w)" , text, re.IGNORECASE))
        d[word] = count;
    return d;