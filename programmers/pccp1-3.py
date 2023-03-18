def solution(queries):
    answer = []
    for gen, n in queries:
        check = 0
        stack = []
        
        n -= 1
        while gen > 1:
            stack.append(n % 4)
            gen -= 1
            n //= 4
        
        while len(stack) > 0:
            num = stack.pop()
            if num == 0:
                answer.append("RR")
                check = 1
                break
            elif num == 3:
                answer.append("rr")
                check = 1
                break
        if check == 0:
            answer.append("Rr")
            
    return answer