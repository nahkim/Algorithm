from heapq import heappop, heappush
import sys
# input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
dict_ = {}
heap = []
res = 1
cnt = 0

for num in nums:
	if dict_[num] not in dict_:
		dict_[num] = 1
	else:
		dict_[num] += 1
	heappush(heap, -num)

while heap:
	tmp = heappop()
	if dict_[tmp] >= 2:
		res *= tmp
		cnt += 1
	if cnt == 2:
		break
print(res)