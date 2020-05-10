output = []

def removeNestings(l):
    global output
    for i in l: 
        if type(i) == list: 
            removeNestings(i) 
        else:
            output.append(i) 

def flat_list(array):
    global output
    output = []
    removeNestings(array)
    return output