def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, v in enumerate(numbers):
        while stack and numbers[stack[-1]] < v:
            answer[stack.pop()] = v
        stack.append(i)
    return answer
