from heapq import heappop, heappush
import sys
# input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

nums_dict = {}
heap = []
res = 1
cnt = 0

for num in nums:
	if num not in nums_dict:
		nums_dict[num] = 1
	else:
		nums_dict[num] += 1
	heappush(heap, -num)

while heap:
	tmp = -heappop(heap)
	if nums_dict[tmp] >= 2:
		print(tmp)
		heappop(heap)
		res *= tmp
		cnt += 1
	if cnt == 2:
		break

if res == 1:
	print(0)
else:
	print(res)