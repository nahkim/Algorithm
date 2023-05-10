import sys
input = sys.stdin.readline

filter_word_len, s_len = map(int, input().split())
filter_word = input().rstrip()
s = input().rstrip()

while filter_word in s:
    s = s.replace(filter_word, '')
        
if s:
    print(s)
else:
    print("EMPTY")