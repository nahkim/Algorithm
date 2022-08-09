# from pprint import pprint
# import sys

# sys.stdin = open('input.txt', 'r')
n = int(input())    # 플레이어 수
res = [0 for _ in range(n)] # 플레이어들의 총 점수입력(0으로 초기화)

matrix = [list(map(int, input().split())) for _ in range(n)]    # 입력값 2차원 배열로 받기
# print(matrix)

# 총 3게임
for k in range(3):  # 총 3게임을 하면서 한게임당 세로줄이 [][k]로 되는 것을 사용
    for i in range(n):  # 특정 플레이어를 기준으로 비교
        for j in range(n):  # 다른 플레이어들과 비교
            check = matrix[i][k]    # 특정 플레이어가 쓴 값
            if i == j:  # 같은 자리에 있는(동일한) 플레이어를 비교할 경우 넘기기
                continue
            if matrix[i][k] == matrix[j][k]:    # 같은 값을 쓴 플레이어가 존재할경우
                check = 0   # 점수 0점으로 만들기
                break       # for j 문 빠져가나기
        res[i] += check     # 특정 플레이어의 점수 더하기

for score in res:           # 각 플레이어의 점수 출력
    print(score)