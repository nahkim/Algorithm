import sys
import heapq

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

lecture_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
lecture_list.sort(key=lambda x : x[1])

lecture_room = []
res = 0

for i, s, e in lecture_list:

    while lecture_room and lecture_room[0] <= s:
        heapq.heappop(lecture_room)
    heapq.heappush(lecture_room, e)
    res = max(res, len(lecture_room))

print(res)