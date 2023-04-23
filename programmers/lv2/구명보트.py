def solution(people, limit):
    answer = 0
    people.sort()
    i = 0
    while people:
        if people[i] <= limit:
            left = people.pop(i)
            if len(people) and left + people[i] <= limit:
                people.pop(i)
            answer += 1
        else:
            people.pop(i)
            answer += 1
    return answer