def solution(s):
    answer = 0
    if s[0] == '+' or s[0] == '-':
        answer = int(s[1:])
        if s[0] == '-':
            answer = -answer
    else:
        answer = int(s)
    return answer