import sys
import heapq

t = int(sys.stdin.readline())

for i in range(t):
    max_heap = []
    min_heap = []

    n = int(sys.stdin.readline())

    check_num = [False] * n

    for num_index in range(n):
        w, num = sys.stdin.readline().split()
        num = int(num)

        if w == "I":
            # 값 삽입
            heapq.heappush(min_heap, (num, num_index))
            heapq.heappush(max_heap, (-num, num_index))
            check_num[num_index] = True

        elif w == "D":
            if num == 1:
                # 최대값 삭제
                while max_heap:
                    output, index = heapq.heappop(max_heap)
                    if check_num[index] == True:
                        check_num[index] = False
                        break
            elif num == -1:
                # 최소값 삭제
                while min_heap:
                    output, index = heapq.heappop(min_heap)
                    if check_num[index] == True:
                        check_num[index] = False
                        break

    while min_heap and check_num[min_heap[0][1]] == False:
        heapq.heappop(min_heap)
    while max_heap and check_num[max_heap[0][1]] == False:
        heapq.heappop(max_heap)
        
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print("EMPTY")