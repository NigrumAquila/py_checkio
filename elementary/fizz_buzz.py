def checkio(number: int) -> str:
    res = str(number);
    if(number % 5 == 0 and number % 3 == 0):
        return "Fizz Buzz";
    elif(number % 3 == 0):
        return "Fizz";
    elif(number % 5 == 0):
        return "Buzz";
    return res;