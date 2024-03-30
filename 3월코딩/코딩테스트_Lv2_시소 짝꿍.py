#미완성
def solution(weights):
    answer = 0
    dic1 = {}
    for weight in weights:
        if weight not in dic1:
            dic1[weight] = 1
        else:
            dic1[weight] += 1
            
        # if weight*(3/2) in weights:
        #     answer+=1
        # if weight*2 in weights:
        #     answer+=1
        # if weight*(4/3) in weights:
        #     answer+=1
            
    for i in dic1:
        answer += int(dic1[i])*(int(dic1[i])-1) / 2
    return answer
