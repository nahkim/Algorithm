from heapq import heappush, heappop

def solution(book_time):
    answer = 0
    heap = []
    time_list = []
    for s, e in book_time:
        time_list.append([int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])])
    time_list.sort(key=lambda x:x[0])

    for time in time_list:
        heappush(heap, time[1])

    for time in time_list:
        s = time[0]
        e = heappop(heap)
        if s < e + 10:
            answer += 1
            heappush(heap, e)
    return answer