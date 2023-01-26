import sys

n = sys.stdin.readline().strip()

arr = []

for i in n:
    arr.append(i)

check_zero = "0"
check_one = "1"
count_zero_start = 0
count_one_start = 0

before_num = arr[0]
if arr[0] == '1':
    count_zero_start += 1
else:
    count_one_start += 1
for i in range(1, len(arr)):
    # 1이면 count 추가
    if check_zero != arr[i]:
        count_zero_start += 1
        if before_num == arr[i]:
            count_zero_start -= 1
    # 0이면 count 추가
    elif check_one != arr[i]:
        count_one_start += 1
        if before_num == arr[i]:
            count_one_start -= 1
    before_num = arr[i]

print(min(count_zero_start, count_one_start))