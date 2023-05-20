from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
minus_heap = []
plus_heap = []

for num in nums:
	if num > 0:
		heappush(plus_heap, num)
	else:
		heappush(minus_heap, -num)

res = []
while plus_heap and minus_heap:
	plus_n = heappop(plus_heap)
	minus_n = -heappop(minus_heap)
	
	if plus_n + minus_n != 0:
		if plus_n > abs(minus_n):
			res.append(minus_n)
			heappush(plus_heap, plus_n)
		else:
			res.append(plus_n)
			heappush(minus_heap, -minus_n)

while plus_heap:
	res.append(heappop(plus_heap))
while minus_heap:
	res.append(-heappop(minus_heap))

print(sum(res))