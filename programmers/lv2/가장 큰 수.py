def solution(numbers):
    answer = ''
    cnt = min(numbers)
    max_cnt = min(numbers)
    num_len = 0

    for n in numbers:
        num_len += len(str(n))
    
    while cnt < 10**num_len:
        check = 1
        for n in numbers:
            if str(n) not in str(cnt):
                check = 0
                break
        if check and max_cnt < cnt:
            max_cnt = cnt
        cnt += 1
    answer = str(max_cnt)
    return answer