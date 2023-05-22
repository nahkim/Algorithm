import sys
input = sys.stdin.readline

MOD = 10 ** 9 + 7

n = int(input())
dp = [0 for i in range(n + 1)]
dp[0] = dp[1] = dp[2] = 1
for i in range(3, n + 1):
	dp[i] = (dp[i - 1] + dp[i - 3]) % MOD
print(dp[n])