def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if i != j and phone_book[j] in phone_book[i]:
                answer = False
                return answer
    return answer