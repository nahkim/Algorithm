list_ = list(map(int, input().split()))

if (sum(list_)) >= 100:
    print('OK')
else:
    min_univ = min(list_)
    num = list_.index(min_uni)
    if num == 0:
        print('Soongsil')
    elif num == 1:
        print('Korea')
    else:
        print('Hanyang')