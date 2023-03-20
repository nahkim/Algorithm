from heapq import heappush, heappop

def solution(ability, number):
    answer = 0
    heap = []
    for n in ability:
        heappush(heap, n)
    for i in range(number):
        n1 = heappop(heap)
        n2 = heappop(heap)
        min_n = n1 + n2
        heappush(heap, min_n)
        heappush(heap, min_n)
    while len(heap) > 0:
        answer += heappop(heap)
    return answer