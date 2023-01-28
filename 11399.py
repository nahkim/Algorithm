import sys
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))

p.sort()
total = 0
tmp = 0
for i in range(n):
    tmp += p[i]
    total += tmp
    
print(total)