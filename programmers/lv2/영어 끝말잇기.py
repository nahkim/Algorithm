def solution(n, words):
    answer = []
    dict_ = {}
    i = 0
    last_word = words[0][0]

    while i < len(words):

        if words[i] not in dict_ and last_word == words[i][0]:
            dict_[words[i]] = 1
            last_word = words[i][-1]
        else:
            play = (i + 1) / n
            if play > (i + 1) // n:
                play += 1
            play = int(play)
            num = i % n + 1
            answer.append(num)
            answer.append(play)
            return answer
        i += 1
    return [0, 0]