import sys

# sys.stdin = open('input.txt', 'r')

list_ = [int(input()) for _ in range(10)]
# print(list_)
average = sum(list_) // 10
mode = list_[0]
count = list_.count(list_[0])
for i in range(10):
    # print(list_[i], ': count : ', list_.count(list_[i]))
    if list_.count(list_[i]) > count:
        # print('count : ', count)
        mode = list_[i]
        count = list_.count(list_[i])
print(average, mode)