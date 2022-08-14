T = int(input())

for test_case in range(T):
    word1, word2 = input().split()
    # 조건 1 : 두 단어의 갯수가 일치해야한다
    if len(word1) != len(word2):
        print(f'{word1} & {word2} are NOT anagrams.')
        continue
    # 조건 2 : word1을 기준으로 같은 문자의 갯수가 같아야한다
    for i in range(len(word1)):
        if word1.count(word1[i]) == word2.count(word1[i]):
            continue
        else:
            print(f'{word1} & {word2} are NOT anagrams.')
            break
    # 모든 문자열을 확인했고 출력이 안됐다면 위의 else문에 들어가지 않았다면 아래 코드로
    else:
        print(f'{word1} & {word2} are anagrams.')