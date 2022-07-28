word = list(input())
# print(word)

res_time = 0

for i in word:
    if (i == 'A' or i == 'B' or i == 'C'):
        res_time += 3
    elif (i == 'D' or i == 'E' or i == 'F'):
        res_time += 4
    elif (i == 'G' or i == 'H' or i == 'I'):
        res_time += 5
    elif (i == 'J' or i == 'K' or i == 'L'):
        res_time += 6
    elif (i == 'M' or i == 'N' or i == 'O'):
        res_time += 7
    elif (i == 'P' or i == 'Q' or i == 'R' or i == 'S'):
        res_time += 8
    elif (i == 'T' or i == 'U' or i == 'V'):
        res_time += 9
    else:
        res_time += 10
print(res_time)