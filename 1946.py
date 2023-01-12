import sys

# sys.stdin = open('input.txt', 'r')

# 테스트 케이스 수
t = int(sys.stdin.readline())

for i in range(t):
    # 지원자 수
    n = int(sys.stdin.readline())
    arr = []
    res = 1
    for j in range(n):
        arr.append(list(map(int, sys.stdin.readline().split())))
    arr.sort()

    # 서류 1등
    search_win = arr[0][1]
    for k in range(1, n):
        if arr[k][1] < search_win:
            res += 1
            search_win = arr[k][1]
    print(res)