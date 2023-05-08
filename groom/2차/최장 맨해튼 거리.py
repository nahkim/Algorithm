import sys

input = sys.stdin.readline
nums = list(map(int, input().split()))
nums.sort()
print(abs(nums[3] - nums[0]) + abs(nums[2] - nums[1]))