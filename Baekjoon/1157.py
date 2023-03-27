word = input()

word_list = {}
# 모든 알파벳 대문자로 변경
word = word.upper()
# 딕셔너리에 알파벳 개수 넣음
for i in range(len(word)):
    if word[i] in word_list:
        word_list[word[i]] += 1
    else:
        word_list[word[i]] = 1

max_key_list = [k for k, v in word_list.items() if (max(word_list.values()) == v)]
# max_list = []
# for k, v in dict_values.items():
#     if v == max(dict_values.values()):
#         max_list.append(k)
if len(max_key_list) > 1:
    print('?')
else:
    print(max_key_list[0])