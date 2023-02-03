import sys
import heapq

n = int(sys.stdin.readline())
heap = []

for i in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))


if n == 1:
    print(0)
else:
    res = 0
    while len(heap) >= 2:
        sm1 = heapq.heappop(heap)
        sm2 = heapq.heappop(heap)
        res += sm1 + sm2
        heapq.heappush(heap, sm1 + sm2)
    print(res)