list_ = [input() for _ in range(5)]

check = 0
for i in range(5):
    if list_[i].count('FBI') == 0:
        continue
    else:
        print(f'{i + 1} ', end='')
        check = 1
if check == 0:
    print('HE GOT AWAY!')