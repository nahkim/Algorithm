answer = list(map(int, input()))
user_input = list(map(int, input()))

def fail():
    for i in range(4):
        if result[i] != 2:
            continue
        while True:
            # 주어진 조건대로 현재 자리 값 + 1 후 10으로 나눈다.
            # 계산한 값이 현재 입력의 다른 자리에 존재한다면 존재하지 않을때까지 반복
            temp = (user_input[i] + 1) % 10
            out = temp not in user_input
            user_input[i] = temp
            if out:
                break

def ball():
    if 1 not in result:
        return
    pos = []
    value = []
    # 위치 옮기기
    for i in range(4):
        if result[i] != 0:
            pos.append(i)
            value.append(user_input[i])
    for i in range(len(pos)):
        # 맨 첫번째 자리일 경우 맨 뒤로 옮겨야 함
        if i == 0:
            user_input[pos[i]] = value[-1]
        else:
            user_input[pos[i]] = value[i - 1]

cnt = 0
while True:
    cnt += 1
    result = [2, 2, 2, 2]

    # 종료 조건
    if user_input == answer:
        print(cnt)
        break

    for i in range(4):
        if user_input[i] in answer:
            if user_input[i] == answer[i]:
                result[i] = 0
            else:
                result[i] = 1
                
    fail()
    ball()