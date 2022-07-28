word = input()
cro_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0
for i in cro_list:
    word = word.replace(i, '*')
# print(word)
print(len(word))