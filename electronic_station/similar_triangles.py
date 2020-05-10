i=__import__
s=lambda T:sorted((z-x)**2+(t-y)**2for(x,y),(z,t)in i('itertools').combinations(T,2))
similar_triangles=lambda*T:len(set(map(i('fractions').Fraction,*map(s,T))))==1