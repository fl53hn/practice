def solution(storey):
    answer = 0
    while storey != 0:
        if storey % 10 > 5:
            answer += (10 - storey%10)
            print((storey + (10 - storey%10))//10) 
            storey = (storey + (10 - storey%10)) // 10
        elif storey%10 <5:
            answer += storey%10
            storey = (storey - storey%10) // 10
        else:
            if (storey//10)%10 >= 5:
                answer += (10 - storey%10)
                storey = (storey + (10 - storey%10)) // 10
            else:
                answer += storey%10
                storey = (storey - storey%10) // 10
    return answer
