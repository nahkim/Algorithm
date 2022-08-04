import sys
# from pprint import pprint

# sys.stdin = open('input.txt', 'r')

T = int(sys.stdin.readline())

for test_case in range(T):
    n, m = map(int, sys.stdin.readline().split())
    matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    transformed_matrix = []
    row = []
    # 리스트 옆으로 돌리기
    for i in range(m):
        for j in range(n - 1, -1, -1):
            # transformed_matrix[i][j] = matrix[j][i]
            row.append(matrix[j][i])
        transformed_matrix.append(row)
        row = []
    # pprint(transformed_matrix)

# 움직인 횟수 = 현재 위치 - 본인 아래(왼쪽)에 있는 박스 갯수
    total = 0
    for i in range(m):
        box_count = sum(transformed_matrix[i])
        for j in range(n - 1, -1, -1):
            if transformed_matrix[i][j] == 1:
                box_count -= 1
                # print('count:' ,j - box_count)
                total += j - box_count
    print(total)