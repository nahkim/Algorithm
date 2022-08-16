# 문자를 카운팅하는 로직
dict_ = {}
while True:
    '''
    예외처리 try ~ except ~
    try : 정상적으로 실행될 때 (오류 X)
    except : 오류가 발생할 때 실행되는 코드 블럭
    '''
    try:
        s = input()
        s_ = s.replace(" ", "")

        # 문자 개수 카운팅
        for w in s_:
            if w in dict_:
                dict_[w] += 1
            else:
                dict_[w] = 1
    except:
        break
sorted_dict = sorted(dict_.items(), key=lambda x: (-x[1], x[0]))
max_ = sorted_dict[0][1]
for char, cnt in sorted_dict:
    if max_ == cnt:
        print(char, end='')