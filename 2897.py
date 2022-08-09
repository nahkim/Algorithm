r, c = map(int, input().split())

parking = [list(input()) for _ in range(r)]

# 자동차 공간을 차지할 델타 (0,0 기준)
# (0,0) (0,1)
# (1,0) (1,1)

dx = [0, 0, 1, 1]
dy = [0, 1, 0, 1]

# 부수고 들어갈 차 갯수만큼 반복문(0 ~ 4대)
for k in range(5):
    # 구하고자하는 총 갯수
    total = 0
    for x in range(r):              # 행 만큼 반복문
        for y in range(c):          # 열 만큼 반복문
            temp_count = 0          # 2 * 2 공간에 들어가 있는 차 수
            check = 0
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if not(0 <= nx < r and 0 <= ny < c):    # 예외 조건(인덱스 범위를 벗어난 경우)
                    check = -1
                    break
                if parking[nx][ny] == '#':              # 예외 조건(빌딩인 경우)
                    temp_count = 0
                    check = -1
                    break
                elif parking[nx][ny] == 'X':            # 주차할 공간에 차가 있다면
                    temp_count += 1                     # 부순 차 더하기
            if check != -1:                             # 예외 조건에 들어갔을 경우 확인하기 위해 사용
                if temp_count == k:                     # 부수고 들어갈 차 갯수 k와 부순 차 temp_count가 같다면
                    total += 1                          # 총 갯수 + 1
    print(total)