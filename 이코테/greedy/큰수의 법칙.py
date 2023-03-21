import sys

n, m, k = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

n_list.sort(reverse=True)
first_n = n_list[0]
second_n = n_list[1]

total = 0
m_count = 0

# 방법 1
for i in range(m):
    if m_count < k:
        total += first_n
        m_count += 1
    else:
        m_count = 0
        total += second_n
        
# 방법 2
count = int(m / (k + 1) * k)
count += m % (k + 1)

total += count * first_n
total += (m - count) * second_n

#####################################
print(total)