def solution(s, skip, index):
    answer = ''
    
    for a in s:
        i = 1
        res_alpha = ''
        check_c = a
        while i < index + 1:
            if check_c == 'z':
                check_c = 'a'
            else:
                ascii = ord(check_c) + 1
                check_c = chr(ascii)

            if check_c in skip:
                continue
            else:
                i += 1
                res_alpha = check_c
        answer += res_alpha
    return answer