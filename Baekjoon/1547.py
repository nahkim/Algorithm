n = int(input())
list_ = [1, 0, 0]

for i in range(n):
    x, y = map(int, input().split())
    list_[x - 1], list_[y - 1] = list_[y - 1], list_[x - 1]
print(list_.index(1) + 1)