list_ = [input() for _ in range(3)]

for word in list_:
    cnt = 1
    max_cnt = 1
    same_word = word[0]
    for i in range(1, len(word)):
        if word[i] == same_word:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
            cnt = 1
            same_word = word[i]
    if max_cnt < cnt:
        max_cnt = cnt
    print(max_cnt)