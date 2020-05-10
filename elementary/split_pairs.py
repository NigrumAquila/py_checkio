def split_pairs(a):
    a+='_'*(len(a)%2)
    return [a[i:i+2] for i in range(0,len(a),2)]