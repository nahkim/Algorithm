n = int(input())

list_ = list(map(int, input().split()))
list_.sort()

res = 0

for i in range(n):
    tmp = list_[:i] + list_[i + 1 :]
    start, end = 0, len(tmp) - 1

    while start < end:
        total = tmp[start] + tmp[end]
        if list_[i] < total:
            end -= 1
        elif list_[i] == total:
            res += 1
            break
        else:
            start += 1
print(res)

# 처음엔 버블정렬하듯이 하나하나 더하고 비교하는 코드로 짰더니 시간초과 발생
# 구하고자하는 숫자를 제외하고 리스트를 만듬
# 새로 만든 리스트에서 2개 숫자를 더해서 비교
