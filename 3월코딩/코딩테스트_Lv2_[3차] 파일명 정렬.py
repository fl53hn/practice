def solution(files):
    answer = []
    ans = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(0, len(files)):
        HEAD, NUMBER, TAIL = '', '', ''
        for j in range(0,len(files[i])):
            if files[i][j] not in numbers:
                if len(NUMBER) == 0:
                    HEAD += files[i][j]
                else:
                    TAIL += files[i][j]
            else:
                if len(TAIL) == 0:
                    NUMBER += files[i][j]
                else:
                    TAIL += files[i][j]
            if j == len(files[i])-1:
                answer.append([HEAD,NUMBER,TAIL])
    answer = sorted(answer, key = lambda x : (x[0].lower(),int(x[1])))
    print(answer)
    for an in range(0, len(answer)):
        ans.append(answer[an][0] + answer[an][1] + answer[an][2])
    return ans
