import re

def double_substring(line):
    matches = re.findall(r'(.+)(?=.*\1)', line)
    largest = '' if not matches else max(matches, key=lambda m: len(m))
    return len(largest)