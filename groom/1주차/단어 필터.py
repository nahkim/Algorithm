import sys
input = sys.stdin.readline

filter_word_len, s_len = map(int, input().split())
filter_word = input().rstrip()
s = input().rstrip()

while filter_word in s:
    idx = s.find(filter_word)
    for _ in range(filter_word_len):
        s = s[:idx] + s[idx + 1:]
        
if s:
    print(s)
else:
    print("EMPTY")