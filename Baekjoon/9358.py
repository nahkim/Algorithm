import sys

def fold(arr):

    if len(arr) == 2:
        return arr

    new_arr = []
    i = 0
    j = len(arr) - 1
    while i <= j:
        new_arr.append(arr[i] + arr[j])
        i += 1
        j -= 1
    return fold(new_arr)


T = int(sys.stdin.readline())

for i in range(1, T + 1):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    new_arr = arr
    while True:
        new_arr = fold(new_arr)
        if len(new_arr) == 2:
            break
    if new_arr[0] > new_arr[1]:
        print("Case #", i, ": Alice", sep="")
    else:
        print("Case #", i, ": Bob", sep="")
    