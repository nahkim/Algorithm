forbidden_word = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

words = input()

for word in words:
    if not word in forbidden_word:
        print(word, end='')