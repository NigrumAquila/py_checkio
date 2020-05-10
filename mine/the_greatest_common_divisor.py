gcd = lambda a, b, *c: c and gcd(a, gcd(b, *c)) or b and gcd(b, a % b) or a
greatest_common_divisor = gcd