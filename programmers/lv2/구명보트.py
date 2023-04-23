from heapq import heappush, heappop

def solution(people, limit):
    answer = 0
    heap = []
    for person in people:
        heappush(heap, person)

    while heap:
        person1 = heappop(heap)
        if heap and person1 <= limit:
            person2 = heappop(heap)
            if (person1 + person2) > limit:
                heappush(heap, person2)
        answer += 1
    return answer