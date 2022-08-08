def find_seven_nanjang(nanjang_list):
    total = 0
    for i in range(len(nanjang_list) - 1):
        for j in range(i + 1, len(nanjang_list)):
            for k in range(len(nanjang_list)):
                if k != i and k != j:
                    total += nanjang_list[k]
            if total == 100:
                res_list = [i, j]
                return res_list
            total = 0

nine_person = []
for i in range(9):
    nine_person.append(int(input()))

nine_person.sort()
res_list = find_seven_nanjang(nine_person)
for i in range(len(nine_person)):
    if i != res_list[0] and i != res_list[1]:
        print(nine_person[i])