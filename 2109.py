import sys
import heapq

n = int(sys.stdin.readline())
lecture = [list(map(int, sys.stdin.readline().split()))  for i in range(n)]

lecture.sort(key=lambda x: x[1])

heap = []

for pay, day in lecture:
    heapq.heappush(heap, pay)

    if day < len(heap):
        heapq.heappop(heap)
print(sum(heap))