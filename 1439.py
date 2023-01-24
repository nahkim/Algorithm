import sys

n = sys.stdin.readline().strip()

arr = []

for i in n:
    arr.append(i)

check_zero = "0"
check_one = "1"
count_zero_start = 0
count_one_start = 0

# 1이면 count 추가
before_num = arr[0]
if arr[0] == '1':
    count_zero_start += 1
for i in range(1, len(arr)):
    if check_zero == arr[i]:
        before_num = arr[i]
        continue
    else:
        count_zero_start += 1
        if before_num == arr[i]:
            count_zero_start -= 1
            continue
        before_num = arr[i]
  
# 0이면 count 추가
before_num = arr[0]
if arr[0] == '0':
    count_one_start += 1
for i in range(1, len(arr)):
    if check_one == arr[i]:
        before_num = arr[i]
        continue
    else:
        count_one_start += 1
        if before_num == arr[i]:
            count_one_start -= 1
            continue
        before_num = arr[i]

print(min(count_zero_start, count_one_start))