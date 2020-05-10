def fast_train(sections):
    limit = sum([[y]*x for x, y in sections], [])+[0]
    run = lambda x: sum([[y]*y for y in range(x, -1, -1)], [])
    time, speed, pos = [0]*3
    while pos < len(limit)-1:
        speed += all(x <= y for x, y in zip(run(speed+1), limit[pos:])) + \
                 all(x <= y for x, y in zip(run(speed), limit[pos:])) - 1
        pos += speed
        time += 1
    return time