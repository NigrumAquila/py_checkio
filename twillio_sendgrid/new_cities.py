def subnetworks(net, crushes):
    segment = []
    for i in range(len(net)):
        one = set(net[i]) - set(crushes)
        for two in segment:
            if one & two:
                two |= one
                one = set()
        if one:
            for k in range(i + 1, len(net)):
                two = set(net[k]) - set(crushes)
                if one & two:
                    one |= two
            segment.append(one)

    return len(segment)