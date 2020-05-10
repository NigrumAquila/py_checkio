import re

def safe_code(equation):
    zero = not([n for n in re.split("=|\+|-|\*|/", equation) if len(n) > 1 and n[:1]=='#'])
    for c in [chr(48+n) for n in range(0 if zero else 1, 10) if chr(48+n) not in equation]:
        if eval(equation.replace('#', c).replace('=', '==')): return int(c)
    return -1