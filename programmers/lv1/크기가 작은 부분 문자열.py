def solution(t, p):
    answer = 0
    t_len = len(t)
    p_len = len(p)
    for i in range(t_len - p_len + 1):
        if p >= t[i:i + p_len]:
            answer += 1
    return answer