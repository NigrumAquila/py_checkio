def checkio(number):
    triangle = number
    saw_list = []
    for n in range(1,triangle):
        saw_list.append(sum(range(n)))
        if saw_list[-1] > triangle: break
        
    for start in range(1,len(saw_list)):
        res = []
        triangle = number
        for n in saw_list[start:-1]:
            triangle -= n
            res.append(n)
            if triangle < 0 : break
            if triangle == 0 : return res
            
    return []