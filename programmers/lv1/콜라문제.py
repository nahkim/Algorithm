def solution(a, b, n):
    answer = 0
    while n >= a:
        using = n // a
        add_coke = using * b
        n -= using * a
        n += add_coke
        answer += add_coke
    return answer