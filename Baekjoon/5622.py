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

# 방법 2
dict_ = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S' : 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
}

word = list(input())
res_time = 0
for i in word:
    number = dict_[i]
    res_time += number + 1
print(res_time)