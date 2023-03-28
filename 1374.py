import sys
import heapq

sys.stdin = open("input.txt", "r")

n = int(sys.stdin.readline())

lecture_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

# print(lecture_list)

lecture_list.sort(key=lambda x : x[1])

lecture_room = []
is_empty = 0

for i, s, e in lecture_list:

    if lecture_room == []:
        heapq.heappush(lecture_room, (-e, s))
        is_empty += 1

    if is_empty > 0:
        heapq.heappush(lecture_room, (-e, s))
        is_empty -= 1
    else:
        tmp = heapq.heappop(lecture_room)
        is_empty += 1
        if -tmp[0] <= s:
            heapq.heappush(lecture_room, (-e, s))
            is_empty -= 1
        else:
            heapq.heappush(lecture_room, (-e, s))

print(len(lecture_room))
            
    
