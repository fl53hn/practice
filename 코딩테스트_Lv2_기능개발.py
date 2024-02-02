def solution(progresses, speeds):
    answer = []
    baepo = []
    count2 = 1
    for i in range(0, len(progresses)):
        a = progresses[i]
        count = 0
        while a<100:
            a += speeds[i]
            count+=1
        baepo.append(count)
    max1 = baepo[0]
    print(baepo)
    for j in range(1,len(baepo)):
        if max1 < baepo[j]:
            answer.append(count2)
            max1 = baepo[j]
            count2 = 1
            if j == len(baepo)-1:
                answer.append(count2)
        else:
            count2+=1
            if j == len(baepo)-1:
                answer.append(count2)
    return answer
