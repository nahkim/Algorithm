T = int(input())

for _ in range(T):
    n = int(input())
    memo1 = list(map(int, input().split()))
    m = int(input())
    memo2 = list(map(int, input().split()))
    dict_memo1 = {}
    for num in memo1:
        dict_memo1[num] = 1
    for num in memo2:
        if num in dict_memo1:
            print(1)
        else:
            print(0)