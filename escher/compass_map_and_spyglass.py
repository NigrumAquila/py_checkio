def navigation(_list):
    location = {j: (index1, index2) for index1, i in enumerate(_list) for index2, j in enumerate(i) if
                j in ['Y', 'C', 'M', 'S']}
    path = map(lambda x: max([abs(x[0] - location.get("Y")[0]), abs(x[1] - location.get("Y")[1])]), location.values())
    return sum(path)