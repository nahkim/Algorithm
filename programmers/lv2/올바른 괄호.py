def solution(s):
    answer = True
    stack = []
    for c in s:
        if c == ')':
            if len(stack) == 0:
                return False
            stack.pop()
        elif c == '(':
            stack.append('(')
    
    if stack:
        return False
    return True