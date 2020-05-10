def checkio(*args):
    size = len(args);
    if(size == 0):
        return 0;
    l = list(args)
    i = 0;
    max = -99999;
    min = 99999;
    idx = size - 1;
    for key in l:
        if(key > max):
            max = key;
        if(key < min):
            min = key;
    res = max - min;
    return res;