class HackerLanguage:
    def __init__(s): s.m, s.c, s.b = "", '1000000', __import__('re').sub
    def write(s, t): s.m += t
    def delete(s, k): s.m = s.m[:-k]
    def send (s): return ''.join([f'{ord(c):07b}',c,s.c][(c<'!')+(c<'A')] for c in s.m)
    def read(s, m): return s.b('[01]'*7, lambda n:[chr(int(n.group(0),2)),' '][n.group(0)==s.c], m)