# import sys
# sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())

res_dict = {}
for i in range(n + m):
    person = input()
    if person in res_dict:
        res_dict[person] += 1
    else:
        res_dict[person] = 1

res_list = []
for key, value in res_dict.items():
    if (value == 2):
        res_list.append(key)

print(len(res_list))
res_list.sort()
for person in res_list:
    print(person)
