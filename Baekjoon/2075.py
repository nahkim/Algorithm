from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for num in tmp:
        # heap의 용량이 n이 넘어가면 pop하여 제일 작은 수부터 제거해줌
        if len(heap) < n:
            heappush(heap, num)
        else:
            if heap[0] < num:
                heappop(heap)
                heappush(heap, num)

# n개 남은 힙에 첫번째가 n번째로 큰수이기 때문에 heap[0]
print(heap[0])