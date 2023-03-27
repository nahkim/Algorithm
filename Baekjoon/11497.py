# 정렬

# 테스트 케이스 갯수
t = int(input())

for i in range(t):
    j = int(input())
    list_ = list(map(int, input().split()))
    list_.sort(reverse=True)
    max_ = list_[j - 2] - list_[j - 1]
    for k in range(j - 2):
        tmp = list_[k] - list_[k + 2]
        if max_ < tmp:
            max_ = tmp
    print(max_)

# 양 옆에 있는 숫자 차의 최댓값을 최소화시켜야함
# 첫번째 숫자와 마지막 숫자도 인접해있는 거라 큰 숫자들을 양 옆에 둬야함
# 리스트 내림차순
# list_[i]와 list_[i + 2]가 인접하고 최대값 구함
