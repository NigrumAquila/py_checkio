t=lambda s: {int(s)}|{x for p in range(1,len(s)) for a in t(s[:p]) for b in t(s[p:]) for x in {a+b,a-b,a*b,a/b if b else 0}}
checkio=lambda d: 100 not in t(d)