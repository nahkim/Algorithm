a, b = map(int, input().split())

x = max(a, b)
y = min(a, b)
while y:
    x, y = y, x % y
gcd = x

lcm = a * b // gcd
print(gcd)
print(lcm)