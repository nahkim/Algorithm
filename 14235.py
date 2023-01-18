import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    
    present = list(map(int, sys.stdin.readline().split()))

    if present[0] == 0:
        if len(heap) > 0:
            max_present = -heapq.heappop(heap)
            print(max_present)
        else:
            print(-1)
    else:
        for j in range(1, present[0] + 1):
            heapq.heappush(heap, -present[j])