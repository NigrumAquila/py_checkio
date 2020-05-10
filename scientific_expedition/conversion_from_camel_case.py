import re

def from_camel_case(name):
    return '_'.join(s.lower() for s in re.findall('([A-Z][a-z]*)', name))