def count_gold(pyramid):
    first = list(pyramid[-1])
    pyramid = pyramid[:-1]
    for i in pyramid[::-1]:
        first = [max(first[j], first[j+1]) + i[j] for j in range(len(i))]
    return max(first)