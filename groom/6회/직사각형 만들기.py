from heapq import heappop, heappush
import sys

n = int(input())
nums = list(map(int, input().split()))

nums_dict = {}
heap = []
pair = []
res = 0

for num in nums:
	if num not in nums_dict:
		nums_dict[num] = 1
	else:
		nums_dict[num] += 1
	heappush(heap, -num)


while heap:
	tmp = -heappop(heap)
	if nums_dict[tmp] >= 2:
		heappop(heap)
		pair.append(tmp)
		nums_dict[tmp] -= 2

for i in range(0, len(pair) // 2 * 2, 2):
	res += pair[i] * pair[i + 1]
	
print(res)
	