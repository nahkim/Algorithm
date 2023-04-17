from heapq import heappush, heappop

def solution(X, Y):
    answer = ''
    heap = []
    dict_x = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    dict_y = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
    for key in X:
        dict_x[key] += 1
    for key in Y:
        dict_y[key] += 1

    for key in X:
        if dict_y[key] >= 1 and dict_x[key] >= 1:
            heappush(heap, -int(key))
            dict_y[key] -= 1
            dict_x[key] -= 1
    if len(heap) == 0:
        return "-1"
    while heap:
        answer += str(-heappop(heap))
    if answer.count("0") == len(answer):
        return "0"
    return answer