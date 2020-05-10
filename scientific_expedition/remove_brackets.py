from itertools import product
brackets = dict(zip('({[', ')}]'))

def remove_brackets(input):
    def is_balanced(s):
        stack = []
        for b in s:
            if b in '([{':
                stack.append(b)
            elif stack and b == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        return not stack
    def delete(mask):
        return ''.join(bracket for bracket, delete in zip(input, mask) if not delete)
    masks = sorted(product((True, False), repeat=len(input)), key=sum)
    return next(result for result in map(delete, masks) if is_balanced(result))