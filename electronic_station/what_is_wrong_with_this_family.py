def is_family(tree):
    f=[a for a,s in tree]
    s=[s for a,s in tree]
    return True if sum(map(lambda x:x in s,set(f)))==len(set(f))-1 and sum(map(lambda x:s.count(x)==1,s))==len(s) and sum(map(lambda x,y:x!=y,f,s))==len(tree) and sum([a for a in map(lambda x:[set(a) for a in tree].count(set(x))==1,tree)])==len(tree)  else False