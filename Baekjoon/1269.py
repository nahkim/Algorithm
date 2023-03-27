import sys

n, m = map(int, sys.stdin.readline().split())

dict = {}
n_list = list(map(int, sys.stdin.readline().split()))
m_list = list(map(int, sys.stdin.readline().split()))
for i in range(len(n_list)):
    if n_list[i] in dict:
        dict[n_list[i]] += 1
    else:
        dict[n_list[i]] = 1
for i in range(len(m_list)):
    if m_list[i] in dict:
        dict[m_list[i]] += 1
    else:
        dict[m_list[i]] = 1
count = 0
for k, v in dict.items():
    if v == 1:
        count +=1
print(count)