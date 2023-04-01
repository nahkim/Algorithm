def solution(name, yearning, photo):
    answer = []
    check = [0] * len(name)
    
    for persons in photo:
        res = 0
        check = [0] * len(name)
        for person in persons:
            for i in range(len(name)):
                if person != name[i] or check[i] == 1:
                    continue
                res += yearning[i]
                check[i] = 1
        answer.append(res)
    return answer