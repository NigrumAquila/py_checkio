def neighbour(n, region, ndict):
    templist = []
    for i in range(len(region)):
        if n in region[i]:
            templist.append([i,region[i].index(n)])
            break
    pointer = 0
    while pointer < len(templist):
        [i,j] = templist[pointer]
        for [k,l] in [[0, -1], [-1, 0], [0, 1], [1, 0]]:
            if (i+k >= 0 
            and i+k < len(region) 
            and j+l >= 0 
            and j+l < len(region[0])):
                if region[i+k][j+l] == n and [i+k,j+l] not in templist:
                    templist.append([i+k,j+l])
                elif region[i+k][j+l] != n and region[i+k][j+l] not in ndict[n]:
                    ndict[n].append(region[i+k][j+l])
        pointer += 1


def color_map(region):
    N = max(max(region[i]) for i in range(len(region)))
    colordict = {}
    ndict = {}
    tasklist = []
    for i in range(N+1):
        colordict[i] = 0
        ndict[i] = []
        tasklist.append(i)
    
    while tasklist:
        n = tasklist.pop(0)
        neighbour(n, region, ndict)

    i = 0
    while i <= N:
        colordict[i] += 1
        if all(colordict[i] != colordict[j] for j in ndict[i]):
            i += 1
            continue
        if colordict[i] == 4:
            colordict[i] = 0
            i -= 1

    return list(colordict.values())