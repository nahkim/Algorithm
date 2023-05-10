import sys
input = sys.stdin.readline

def make_prime(n):
	is_prime = [1 for _ in range(n + 1)]
	prime = []
	for i in range(2, n + 1):
		if not is_prime[i]:
			continue
		prime.append(i)
		for j in range(i * 2, n + 1, i):
			is_prime[j] = 0
	return prime

n = int(input())
nums = [0] + list(map(int, input().split()))
res = 0

primes = make_prime(n)
for prime in primes:
		res += nums[prime]
print(res)