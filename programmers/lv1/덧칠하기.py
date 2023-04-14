def solution(n, m, section):
    answer = 0
    i = section[0]
    
    if m == 1:
        return len(section)
    
    for j in section:
        if answer == 0:
            i = j + m - 1
            answer += 1
        if i < j:
            i = j + m - 1
            answer += 1
    return answer