import re

def textual(number):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    return re.sub("\ +", " ", (ones[number//1000] + " thousand " if number // 1000 > 0 else "") \
    +                         (ones[(number%1000)//100] + " hundred " if number%1000 // 100 > 0 else "") \
    +                         (tens[(number%100) // 10] + " " if number % 100 >= 20 else "") \
    +                         (teens[(number%100) - 10] if number % 100 >= 10 and number % 100 < 20 else "") \
    +                         (ones[number%10] if number % 100 < 10 or number % 100 >= 20 else "")).strip() if number != 0 else "zero"

def secret_room(number):
    return sorted(range(1, number + 1), key=textual).index(number) + 1