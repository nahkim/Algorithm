def solution(text, anagram, sw):
    answer = ''
    if sw == True:
        for i in range(len(text)):
            for n in range(len(anagram)):
                if anagram[n] == i:
                    answer += text[n]
                    break
    else:
        for num in anagram:
            answer += text[num]
    return answer