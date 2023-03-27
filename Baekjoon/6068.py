import sys
import heapq

n = int(sys.stdin.readline())
heap = []

# 마감 시간 기준으로 최대힙
for i in range(n):
    t, e = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (-e, t))


last = heapq.heappop(heap)
last_time = abs(last[0] + last[1])
while heap:
    last = heapq.heappop(heap)
    if -last[0] >= last_time:
        last_time -= last[1]
    # 마감 시간보다 현재 남은 시간이 클 경우
    else:
        last_time = -last[0]
        last_time -= last[1]

# 제시간에 끝낼 수 없는 경우
if last_time < 0:
    print(-1)
else:
    print(last_time)