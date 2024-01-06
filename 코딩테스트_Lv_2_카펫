def solution(brown, yellow):
    answer = []
    OLIVE = 0
    OLIVE = brown + yellow
    for i in range(1, OLIVE):
        
        if OLIVE % i == 0:
            j = OLIVE / i
            if (i-2)*(j-2) == yellow and (2*(i+j) - 4) == brown:
                answer.append(j)
                answer.append(i)
                break
            else:
                continue
    return answer
