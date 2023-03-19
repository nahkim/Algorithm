def solution(command):
    answer = [0, 0]
    # check = [y + 1, x + 1, y - 1, x - 1]
    
    check1 = ['y', 'x', 'y', 'x']
    check2 = [1, 1, -1, -1]
    
    rotate_num = 0
    for c in command:
        if c == "R":
            rotate_num += 1
        elif c == "L":
            if rotate_num == 0:
                rotate_num = 3
            else:
                rotate_num -= 1
        elif c == "G":
            rotate = abs(rotate_num) % 4
            if rotate == 0 or rotate == 2:
                answer[1] += check2[rotate]
            else:
                answer[0] += check2[rotate]
        else:
            rotate = abs(rotate_num) % 4
            if rotate == 0 or rotate == 2:
                answer[1] -= check2[rotate]
            else:
                answer[0] -= check2[rotate]
        
    return answer