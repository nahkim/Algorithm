import sys

n = int(sys.stdin.readline())

list_ = [int(sys.stdin.readline()) for i in range(n)]

list_.sort()

# 산술평균
mean = round(sum(list_) / n)
print(mean)

# 중앙값
median = list_[n // 2]
print(median)

# 최빈값
res_list = []
dict_ = {}
for num in list_:
    if num in dict_:
        dict_[num] += 1
    else:
        dict_[num] = 1
for k, v in dict_.items():
    if v == max(dict_.values()):
        res_list.append(k)
if len(res_list) == 1:
    print(res_list[0])
else:
    print(res_list[1])

# 범위
print(list_[-1] - list_[0])
