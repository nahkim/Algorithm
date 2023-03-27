# 차 갯수마다 요금 입력값
price1, price2, price3 = map(int, input().split())

# 총 요금
total = 0

# 3대의 차가 주차장에 들어갔다 나온 시간 리스트화
list_ = []

#입력값 받기
for _ in range(3):
    list_.append(list(map(int, input().split())))

# 마지막으로 나가는 차 시간
last_time = max(list_[0][1], list_[1][1], list_[2][1])

# 각 차들이 들어온 시간을 나타내기 위해 리스트로 만들기
A = [0 for _ in range(last_time + 1)]
B = [0 for _ in range(last_time + 1)]
C = [0 for _ in range(last_time + 1)]

# 차가 주차장에 들어가있는 시간을 1로 변경
for i in range(list_[0][0], list_[0][1]):
    A[i] = 1
for i in range(list_[1][0], list_[1][1]):
    B[i] = 1
for i in range(list_[2][0], list_[2][1]):
    C[i] = 1

# 차가 들어온 시간부터 모든 차가 나갈때까지 반복문
for i in range(last_time):
    # 주차장에 있는 차의 갯수만큼 요금 더하기
    if A[i] + B[i] + C[i] == 1:
        total += price1
    elif A[i] + B[i] + C[i] == 2:
        total += price2 * 2
    elif A[i] + B[i] + C[i] == 3:
        total += price3 * 3
print(total)