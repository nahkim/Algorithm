s = input()
happy = s.count(':-)')
sad = s.count(':-(')
if happy == sad:
    if happy == 0:
        print('none')
    else:
        print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')