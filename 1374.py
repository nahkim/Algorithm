import sys
import heapq

# sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

lecture_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

lecture_room = []
tmp = []

for i, s, e in lecture_list:
    heapq.heappush(lecture_room, (s, e))

s, e = heapq.heappop(lecture_room)
heapq.heappush(tmp, e)

while lecture_room:
    e = tmp[0]
    ls, le = heapq.heappop(lecture_room)
    if e <= ls:
        heapq.heappop(tmp)
    heapq.heappush(tmp, le)

print(len(tmp))