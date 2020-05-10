import string


def check_pangram(text):
    return all([char in text.lower() for char in string.ascii_lowercase])