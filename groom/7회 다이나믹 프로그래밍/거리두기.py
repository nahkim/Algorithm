import sys
sys.setrecursionlimit(150000)

import resource
resource.setrlimit(resource.RLIMIT_STACK, (64 * 1024 * 1024, -1))

MOD = 10**8 + 7
N = int(input())
dp = dict()
for n in range(5):
    dp[(0, n)] = 1 if n == 0 else 0

def get(i, n):
    if (i, n) in dp:
        return dp[(i, n)]
    ret = 0
    if n == 0:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 2) + get(i - 1, 3) + get(i - 1, 4)
    elif n == 1:
        ret += get(i - 1, 0) + get(i - 1, 2) + get(i - 1, 3)
    elif n == 2:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 3) + get(i - 1, 4)
    elif n == 3:
        ret += get(i - 1, 0) + get(i - 1, 1) + get(i - 1, 2)
    else:
        ret += get(i - 1, 0) + get(i - 1, 2)
    ret %= MOD
    dp[(i, n)] = ret
    return ret
    
res = 0
for n in range(5):
    res += get(N, n)
print(res % MOD)