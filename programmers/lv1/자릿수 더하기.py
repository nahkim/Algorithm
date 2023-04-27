def solution(n):
    answer = 0
    while n > 0:
        t = n % 10
        answer += t
        n //= 10
    return answer