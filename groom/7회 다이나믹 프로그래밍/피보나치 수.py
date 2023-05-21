import sys
sys.setrecursionlimit(111111)

# 위의 코드를 그냥 실행하면 스택 메모리 제한으로 인해 일부 테스트 케이스를 통과 불가
# 아래 주석 처리된 코드와 같이 실행하면, 스택 메모리 제한을 임시적으로 조금 늘려서 문제를 해결할 수 있음
# 하지만 시스템에 직접 접근하는 코드이므로, 일반적으로 코딩 테스트를 응시할 때는 사용하면 안되는 코드임

'''
import resource
resource.setrlimit(resource.RLIMIT_STACK, (64 * 1024 * 1024, -1))
'''

MOD = 10**9 + 7
F = [-1 for _ in range(100008)]

def fib(n):
    if F[n] != -1:
        return F[n]
    if n <= 2:
        return 1
    F[n] = (fib(n - 1) + fib(n - 2)) % MOD
    return F[n]
    
N = int(input())
print(fib(N))