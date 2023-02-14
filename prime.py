def solution(num_list):
    answer = []
    check = 0
    for num in num_list:
        for i in range(2, num - 1):
            if num % i == 0:
                check = 1
                if num == 2:
                    check = 0
                break
        if check == 0:
            answer.append(True)
        else:
            answer.append(False)
        check = 0
    return answer