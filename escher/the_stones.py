def stones(pile, moves):
    L = {1}
    for i in range(2, pile+1):
        if not({i-j for j in moves} & L): L = L | {i}
    return (pile in L)+1