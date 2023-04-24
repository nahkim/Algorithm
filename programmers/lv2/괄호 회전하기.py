from collections import deque

def check_symmetry(s):
    stack = []
    
    for c in s:
        if stack:
            if c == ')':
                c_pop = stack.pop()
                if len(stack) == 0 and c_pop != '(':
                    return False
            elif c == '}':
                c_pop = stack.pop()
                if len(stack) == 0 and c_pop != '{':
                    return False
            elif c == ']':
                c_pop = stack.pop()
                if len(stack) == 0 and c_pop != '[':
                    return False
            else:
                stack.append(c)
        else:
            stack.append(c)
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    dq = deque(s)
    dq_len = len(dq)
    for i in range(dq_len):
        if check_symmetry(dq) == True:
            answer += 1
        pop_c = dq.popleft()
        dq.append(pop_c)
    return answer