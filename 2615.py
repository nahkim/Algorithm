import sys
from pprint import pprint
sys.stdin = open('input.txt', 'r')


# 8방을 다 보고 같은 색깔의 바둑돌이 있을 경우 세어나감
# 1 2 3         [-1, -1] [-1, 0] [-1, +1]
# 4 i 5         [0, -1]     i    [0, +1]
# 6 7 8         [+1, -1] [+1, 0] [+1, +1]

# 그러나 위에서부터 왼쪽으로 확인을 할것이기 때문에 4, 6, 7, 8번만 확인하면 됨
# + 가장 왼쪽에 있고 가장 위에 있는 위치에 있는 알을 출력해야하기때문에!



# 6알 이상이 연속적으로 놓인 경우 이긴 것이 아니다 -> 무조건 5알만 가능한건가..?
# 0이 아닌 수가 나올때까지 찾음
# 만약 1(2)이 라면 그 자리 저장후 왼쪽부터 8번 반복해서 8방에 같은 수가 있는지 확인하고 숫자세기 같은 수가 아니라면 멈춤
# 숫자를 셋는데 5라면 이긴것
# 다 돌았는데도 이긴 사람이 없으면 0 출력
def who_is_winner(checkerboard):
    dx = [0, 1, 1, 1]
    dy = [-1, -1, 0, 1]
    find_location = []
    count = 1
    for x in range(19):
        for y in range(19):
            if checkerboard[x][y] != 0:
                check = checkerboard[x][y]
                find_location.append(x)
                find_location.append(y)
                # print(x, y)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    while 0 <= nx < 19 and 0 <= ny < 19:
                        if checkerboard[nx][ny] == check:
                            count += 1
                            nx += dx[k]
                            ny += dy[k]
                            # print(nx, ny)
                            # print(count)
                        else:
                            if count == 5:
                                find_location.append(check) # 맨 앞에 넣어야함 아니면 리턴값 어떻게할지 다시 생각해보기
                                return find_location
                            else:
                                count = 1
                                break
    return [0]

checkerboard = [list(map(int, input().split())) for _ in range(19)]
# pprint(checkerboard)

res = who_is_winner(checkerboard)
if len(res) == 1:
    print(0)
else:
    for i in range(len(res)):
        if i == 0:
            print(res[i])
        else:
            print(res[i], end=' ')