n = int(input())

for _ in range(n):
    list_ = list(input().split())
    for word in list_:
        # print(word)
        print(word[::-1], end=' ')
    print()