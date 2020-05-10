def letter_queue(commands):
    result = ''
    for i in commands:
        if 'PUSH' in i: result += i[-1]
        else: result = result[1:]
    return result