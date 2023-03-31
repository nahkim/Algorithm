# sys.stdin = open('input.txt', 'r')
num = int(input())

res_dict = {}
for i in range(num):
    person, status = input().split()
    if status == 'enter':
        res_dict[person] = 1
    else:
        res_dict[person] = 0
sorted_dict = sorted(res_dict.items(), reverse=True)
for person in sorted_dict:
    if (person[1] == 1):
        print(person[0])