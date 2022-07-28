# import sys
# sys.stdin = open("input.txt", "r")

n = int(input())

book_dict = {}
for i in range(n):
    name = input()
    if name in book_dict:
        book_dict[name] += 1
    else:
        book_dict[name] = 1

max_value = max(book_dict.values())

res_list = []
for key, value in book_dict.items():
    if value == max_value:
        res_list.append(key)

res_list.sort()
print(res_list[0])