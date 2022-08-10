r, c = map(int, input().split())

parking = [list(input()) for _ in range(r)]

# 자동차 공간을 차지할 델타 (0,0 기준)
# (0,0) (0,1)
# (1,0) (1,1)

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

# # 부수고 들어갈 차 갯수만큼 반복문(0 ~ 4대)
# for k in range(5):
#     # 구하고자하는 총 갯수
#     total = 0
#     for x in range(r):              # 행 만큼 반복문
#         for y in range(c):          # 열 만큼 반복문
#             break_count = 0          # 2 * 2 공간에 들어가 있는 차 수
#             if parking[x][y] == '#':
#                 continue
#             for d in range(4):
#                 nx = x + dx[d]
#                 ny = y + dy[d]
#                 if not(0 <= nx < r and 0 <= ny < c):    # 예외 조건(인덱스 범위를 벗어난 경우)
#                     break
#                 if parking[nx][ny] == '#':              # 예외 조건(빌딩인 경우)
#                     break_count = 0
#                     break
#                 elif parking[nx][ny] == 'X':            # 주차할 공간에 차가 있다면
#                     break_count += 1                     # 부순 차 더하기
#             else:                                       # 예외 조건에 들어가지 않았을 경우
#                 if break_count == k:                     # 부수고 들어갈 차 갯수 k와 부순 차 break_count가 같다면
#                     total += 1                          # 총 갯수 + 1
#     print(total)

# 조금 더 효율적인 방법
res = [0] * 5
for x in range(r):              # 행 만큼 반복문
    for y in range(c):          # 열 만큼 반복문
        break_count = 0         # 2 * 2 공간에 들어가 있는 차 수
        if parking[x][y] == '#':
            continue
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if not(0 <= nx < r and 0 <= ny < c):    # 예외 조건(인덱스 범위를 벗어난 경우)
                break
            if parking[nx][ny] == '#':              # 예외 조건(빌딩인 경우)
                break_count = 0
                break
            elif parking[nx][ny] == 'X':            # 주차할 공간에 차가 있다면
                break_count += 1                    # 부순 차 더하기
        else:                                       # 예외 조건에 들어가지 않았을 경우
            res[break_count] += 1                   # res 부순차의 갯수 + 1
for i in res:
    print(i)