import sys
import heapq
import math

t = int(sys.stdin.readline())

for i in range(t):
    arr = []
    n = int(sys.stdin.readline())
    if n > 10:
        k = math.ceil(n / 10)
        for i in range(k):
            arr += list(map(int, sys.stdin.readline().split()))
    else:
        arr = list(map(int, sys.stdin.readline().split()))
    m = arr[0]
    big = 0
    small = 0
    big_heap = []
    small_heap = []
    res = []
    for j in range(n):
        if j % 2 == 0:
            if j == 0:
                res.append(m)
            else:
                if m < arr[j]:
                    big += 1
                    heapq.heappush(big_heap, arr[j])
                else:
                    small += 1
                    heapq.heappush(small_heap, -arr[j])

                if big == 2:
                    # 최소힙
                    heapq.heappush(small_heap, -m)
                    m = heapq.heappop(big_heap)
                elif small == 2:
                    # 최대힙
                    heapq.heappush(big_heap, m)
                    m = -heapq.heappop(small_heap)
                big = 0
                small = 0
                res.append(m)
        else:
            if m < arr[j]:
                big += 1
                heapq.heappush(big_heap, arr[j])
            else:
                small += 1
                heapq.heappush(small_heap, -arr[j])
    
    print(len(res))
    for i in range(len(res)):
        if i != 0 and i % 9 == 0:
            print(res[i])
        else:
            print(res[i], end=" ")
    
    # print(len(res))
    # for i in range(len(res)):
    #     print(res[i], end=" ")
    #     if i != 0 and i % 9 == 0:
    #         print()
    # print()