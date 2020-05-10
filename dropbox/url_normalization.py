import re

def checkio(url):
    def decode(match):
        if '%' not in match.group(): return ''
        encoded = match.group().upper()
        char = chr(int(encoded[1:], 16)).lower()
        return char if re.match('\w|[-~.]', char, re.A) else encoded

    return re.sub(r'%..|/(\w+/\.)?\.|:80(?!\d)', decode, url.lower())