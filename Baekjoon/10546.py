# pypy3로 풀어야함

n = int(input())

dict_ = {}
for i in range(n):
    member = input()
    if member in dict_:
        dict_[member] += 1
    else:
        dict_[member] = 1
for i in range(n - 1):
    member = input()
    dict_[member] -= 1

for k, v in dict_.items():
    if v == 1:
        print(k)
        break