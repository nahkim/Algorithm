import sys

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
res = 0
for num in nums:
	res += num
print(format(res, 'o'))