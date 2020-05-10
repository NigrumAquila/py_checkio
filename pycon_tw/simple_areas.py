import math

def simple_areas(*args):
    if len(args) == 3:
        a = args[0]
        b = args[1]
        c = args[2]
        p=(a+b+c)/2.0
        return math.sqrt((p*(p-a)*(p-b)*(p-c)))  #12*9*8*7
    elif len(args) == 2:
        return args[0]*args[1]
    else:
        return ((args[0]/2.0)**2)*math.pi
