from itertools import combinations
from collections import Counter

tower = lambda cubes: Counter( [''.join(sorted(x)) for faces in 
                        [(''.join(sorted(c[0]+c[3])), 
                          ''.join(sorted(c[1]+c[2])), 
                          ''.join(sorted(c[4]+c[5]))) for c in cubes] 
                        for x in combinations(faces, r=2)] ).most_common()[0][1]