a = ['a', 'e', 'i', 'o', 'u']

while True:
    s = input()
    s = s.lower()
    count_ = 0
    if '#' == s:
        break
    for i in a:
        count_ += s.count(i)
    print(count_)