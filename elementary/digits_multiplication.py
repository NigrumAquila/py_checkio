from functools import reduce

def checkio(number: int) -> int:
    cond = pow(10, 6);
    if(0 < number and number < cond):
        res = 1;
        excList = str(number).replace('0', '');
        intList = list(map(int, excList));
        for x in intList:
            res = res * x;
    return res;