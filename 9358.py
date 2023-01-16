import sys

# sys.stdin = open("input.txt", "r")

def fold(n, arr):
    new_arr = []

    if n % 2 == 1:
        cnt = n // 2 + 1
    else:
        cnt = n // 2
    i = 0
    j = n - 1
    while i <= j:
        new_arr.append(arr[i] + arr[j])
        i += 1
        j -= 1
    return new_arr


T = int(sys.stdin.readline())

for i in range(1, T + 1):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    new_arr = arr
    while True:
        new_arr = fold(len(new_arr), new_arr)
        if len(new_arr) == 2:
            break
    if new_arr[0] > new_arr[1]:
        print("Case #", T, ": Alice", sep="")
    else:
        print("Case #", T, ": Bob", sep="")
    