def solution(want, number, discount):
    answer = 0
    dic = {}
    for i in range(len(number)):
        dic[want[i]] = number[i]
    for i in range(0, len(discount)-9):
        dict = {}
        for num in discount[i:10+i]:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        if dic==dict:
            answer+=1
    return answer
