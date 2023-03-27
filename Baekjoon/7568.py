# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())
people_info = []
ranks = []
for i in range(T):
    x, y = map(int, input().split())
    people_info.append((x, y))
    # print(people_info)
    # print(len(people_info))
rank = 1
for i in people_info:
    for j in people_info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')
    rank = 1