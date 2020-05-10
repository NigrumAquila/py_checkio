def checkio(data):
    s = sum(data)
    dp = [True] + [False for _ in range(s)]
    for i in data:
        for j in range(s,-1,-1):
            if j >= i and dp[j-i]: dp[j] = True
    
    for i in range((s+1)//2,s+1):
        if dp[i]: return abs(s-i*2)
    return -1