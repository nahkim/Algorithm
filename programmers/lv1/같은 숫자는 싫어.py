def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        for j in range(i + 1, len(arr) - 1):
            if arr[i] != arr[j]:
                answer.append(arr[i])
                i = j - 1
                break
        i += 1
    if arr[len(arr) - 1] == arr[len(arr) - 2]:
        answer.append(arr[len(arr) - 2])
    else:
        answer.append(arr[len(arr) - 2])
        answer.append(arr[len(arr) - 1])
    return answer