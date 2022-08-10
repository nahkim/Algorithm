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