def non_repeat(line):
    ls = [line[i:j] for i in range(len(line)) 
                    for j in range(i+1, len(line)+1)
                    if len(set(line[i:j])) == j - i]
    return max(ls, key=len, default='')