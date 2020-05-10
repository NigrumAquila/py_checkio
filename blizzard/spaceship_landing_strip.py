def checkio(landing_map):
    W,H = len(landing_map[0]),len(landing_map)
    bestArea = 0
    for C1 in range(W):
        for C2 in range(C1,W):
            for R1 in range(H):
                for R2 in range(R1,H):
                    if all(landing_map[R][C] in "GS" for R in range(R1,R2+1) for C in range(C1,C2+1)):
                        bestArea = max(bestArea,(R2-R1+1)*(C2-C1+1))
    return bestArea