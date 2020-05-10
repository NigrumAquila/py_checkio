def checkio(first, second):
    total = 0
    for operator in ('&', '|', '^'):
        tot_row = 0
        for i in bin(first)[2:]:
            row = ''
            for j in bin(second)[2:]:
                row += eval('str(int(i) {} int(j))'.format(operator))
            tot_row += int(row, 2)
        total += tot_row
    return total