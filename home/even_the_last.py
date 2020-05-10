def checkio(arr):
    sum = 0;
    temp = 0;
    i = 0;
    lastElem = 0;
    if(len(arr) != 0):
        lastElem = arr[len(arr) - 1];
    while(i < len(arr)):
        sum += arr[i];
        i += 2;
    sum *= lastElem;
    return sum;