def caps_lock(text: str) -> str:
    return "".join(fragment.upper() if i%2 == 1 else fragment for i, fragment in enumerate(text.split('a')))