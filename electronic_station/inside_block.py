def is_inside(ngon, pt):
    ngon = [(x-pt[0], y-pt[1]) for x, y in ngon]
    count = 0
    for (xA, yA), (xB, yB) in zip(ngon, ngon[1:] + ngon[:1]):
        if xA*xB <= 0 and yA*yB <= 0 and yA*xB==yB*xA:
            return True
        count += min(yA,yB) <= 0 < max(yA,yB) and (yA*xB-yB*xA)/(yA-yB) < 0
    return count%2