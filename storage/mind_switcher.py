def mind_switcher(journal):
    NIKOLA, SOPHIA = "nikola", "sophia"
    mind, log = {}, []
    
    def swap(a, b, add_to_log=True):
        mind[a], mind[b] = mind.get(b, b), mind.get(a, a)
        if add_to_log:
            log.append({a, b})
      
    for a, b in journal:
        swap(a, b, add_to_log=False)
        
    robots = set(mind)
    while robots:
        robot = robots.pop()
        robot_mind = mind[robot]
        if robot_mind != robot:
            swap(NIKOLA, robot)
            swap(SOPHIA, robot_mind)
            while mind[SOPHIA] != robot:
                swap(SOPHIA, mind[SOPHIA])
            swap(SOPHIA, robot)
            swap(NIKOLA, robot_mind)
    if mind[NIKOLA] == SOPHIA:
        swap(NIKOLA, SOPHIA)
    return log