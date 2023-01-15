import sys

# sys.stdin = open("input.txt", "r")

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    arr = []
    for i in range(n):
        word = sys.stdin.readline().strip()
        arr.append(word)

    first_num = 0
    i = 0
    first_word = arr[i]
    first_word = first_word.lower()
    
    while i < n:
        tmp = arr[i]
        tmp = tmp.lower()
        if first_word > tmp:
            first_word = tmp
            first_num = i
        i += 1
    print(arr[first_num])
