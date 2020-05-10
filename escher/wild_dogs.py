def wild_dogs(dogs):
    dist = mx = 0
    for p1 in dogs:
        for p2 in dogs:
            if p1 != p2:
                a, b, c = p1[1] - p2[1], p2[0] - p1[0], p1[0] * p2[1] - p2[0] * p1[1]
                count = sum(1 for p in dogs if a * p[0] + b * p[1] + c == 0)
                d = round(abs(c) / (a ** 2 + b ** 2) ** 0.5, 2)
                if (count > mx) or (count == mx and d < dist):
                    mx = count
                    dist = d
    return dist