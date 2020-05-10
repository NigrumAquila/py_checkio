def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.find(begin)+len(begin):text.rfind(end)]