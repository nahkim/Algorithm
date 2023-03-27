list_ = [list(map(int, input().split())) for _ in range(5)]

win_num = 0
win_score = 0
count = 1

for person in list_:
    if sum(person) > win_score:
        win_score = sum(person)
        win_num = count
    count += 1
print(win_num, win_score)