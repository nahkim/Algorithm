n = int(input())

num_dict = {}
for i in range(n):
    num = int(input())
    if num in num_dict:
        num_dict[num] += 1
    else:
        num_dict[num] = 1
max_value = max(num_dict.values())

max_list = []
for k, v in num_dict.items():
    if v == max_value:
        max_list.append(k)

max_list.sort()
print(max_list[0])