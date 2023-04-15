import sys
from heapq import heappush, heappop

input = sys.stdin.readline

heap = []
n = int(input())

for _ in range(n):
    num = int(input())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(-heappop(heap))
    else:
        heappush(heap, -num)