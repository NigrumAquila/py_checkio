def to_camel_case(name):
    return ''.join(ch for ch in name.title() if not ch == '_')