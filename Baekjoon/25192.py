n = int(input())
count = 0
check = 0
dict_ = {}
for _ in range(n):
    chat = input()
    if chat == 'ENTER':
        check = 1
        dict_ = {}
    elif check == 1:
        if not chat in dict_:
            dict_[chat] = 1
            count += 1
print(count)