def steps_to_convert(line1, line2):
    changes = lambda pos1, pos2, size: max(len(line1), len(line2)) if pos2 == -1 else max(pos1, pos2) + max(len(line1) - pos1 - size, len(line2) - pos2 - size)
    return min([changes(i, line2.find(line1[i:k]), k - i) for i in range(len(line1) + 1) for k in range(i, len(line1) + 1)])