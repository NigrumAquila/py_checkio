def digit_stack(commands):
    value, stack = 0, []
    for cmd in commands:
        if ' ' in cmd:
            stack.append(int(cmd[-1]))
        elif stack:
            value += stack[-1] if cmd == 'PEEK' else stack.pop()    
    return value