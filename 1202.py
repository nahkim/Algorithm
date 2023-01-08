import sys
import heapq

N, B = map(int, sys.stdin.readline().split())

heap = []

for i in range(N):
    heapq.heappush(heap, list(map(int, sys.stdin.readline().split())))

B_list = [int(sys.stdin.readline()) for i in range(B)]
B_list.sort()

res = 0
tmp_heap = []

# 적게 나가는 가방 무게부터 탐색
for B_weight in B_list:
    # 아직 넣지 못한 보석이 있고, 가방 무게보다 작거나 같은 보석이라면
    while heap and B_weight >= heap[0][0]:
        heapq.heappush(tmp_heap, -heapq.heappop(heap)[1])
    if tmp_heap:
        # 기본적으로 최소힙으로 작동하기 때문에 21번째 줄에 -를 붙임
        res += -heapq.heappop(tmp_heap)
print(res)
