def between_markers(text: str, begin: str, end: str) -> str:
    start = 0
    try:
        start = text.index(begin) + len(begin);
    except:
        start = 0;
    try:
        end = text.index(end)
    except:
        end = len(text)
    return text[start:end];