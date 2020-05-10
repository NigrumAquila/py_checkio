def checkio(d):
    return abs(sum(d[i-1][0]*d[i][1]-d[i][0]*d[i-1][1] for i in range(len(d))))/2