
word = input()
count = 0
i = 0
while i < len(word):
    if len(word) - i <= 1:
        count += 1
        i += 1
        continue
    if (word[i] == 'c'):
        if word[i + 1] == '=':
            count += 1
            i += 2
            continue
        if word[i + 1] == '-':
            count += 1
            i += 2
            continue
    elif (word[i] == 'd'):
        if word[i + 1] == 'z':
            if (len(word) - (i + 1) == 1):
                count += 1
                i += 1
                continue
            print(word[i + 2])
            if [i + 2] == '=':
                count += 1
                i += 3
                continue
        if word[i + 1] == '-':
            count += 1
            i += 2
            continue
    elif (word[i] == 'l'):
        if word[i + 1] == 'j':
            count += 1
            i += 2
            continue
    elif (word[i] == 'n'):
        if word[i + 1] == 'j':
            count += 1
            i += 2
            continue
    elif (word[i] == 's'):
        if word[i + 1] == '=':
            count += 1
            i += 2
            continue
    elif (word[i] == 'z'):
        if word[i + 1] == '=':
            count += 1
            i += 2
            continue
    count += 1
    i += 1
print(count)