import sys

target, start = map(int, sys.stdin.readline().split())
count = 0

while start != target:
    if start // 2 < target:
        while start != target:
            start -= 1
            count += 1

    elif start % 2 == 0:
        start = start // 2
        count += 1
    else:
        start -= 1
        count += 1
print(count)