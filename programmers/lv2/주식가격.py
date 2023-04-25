from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        price = q.popleft()
        cnt = 0
        for p in q:
            cnt += 1
            if price > p:
                break
        answer.append(cnt)
    return answer