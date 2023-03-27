t = int(input())
pc = [0 for _ in range(100)]
n = list(map(int, input().split()))
count = 0
for i in n:
    if pc[i - 1] != 0:
        count += 1
    pc[i - 1] = 1
print(count)