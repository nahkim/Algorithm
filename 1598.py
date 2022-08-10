# 1줄에 4개씩 들어간다
# [1 2 3 4] 로 4로 나누게되면
# [0 0 0 1] 몫
# [1 2 3 0] 나머지
# 결국 몫과 나머지 차이가 직각의 거리가 된다
# 마지막에 4로 나누어 떨어지는 값들을 변경해야한다

first, second = map(int, input().split())

div1, mod1 = divmod(first, 4)
div2, mod2 = divmod(second, 4)
if first % 4 == 0:
    div1 -= 1
    mod1 = 4
if second % 4 == 0:
    div2 -= 1
    mod2 = 4
div = abs(div1 - div2)
mod = abs(mod1 - mod2)
print(div + mod)