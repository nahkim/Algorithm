def solution(input_string):
    answer = ''
    
    dict_ = {}
    for i in range(len(input_string)):
        if input_string[i] in dict_:
            dict_[input_string[i]] += 1
        else:
            dict_[input_string[i]] = 1
            
    for i in range(len(input_string)):
        count = 0
        
        if dict_[input_string[i]] == -1:
            continue
        elif dict_[input_string[i]] > 1:
            for j in range(dict_[input_string[i]]):
                if input_string[i] == input_string[i + j]:
                    count += 1
                else:
                    answer += input_string[i]
                    break
            dict_[input_string[i]] = -1
    
    if answer == "":
        return "N"
    answer = "".join(sorted(answer))
    return answer