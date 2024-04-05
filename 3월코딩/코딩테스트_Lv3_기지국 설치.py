import math
# 1. 그리디?
# N: 200,000,000
# 1 ~ (2*w)+1 설치, 6~10 사이 있음, 
def solution(n, stations, w):
    i,j = 1, 0
    answer = 0
    while i <= n:
        if (i + (2*w)) >= max(1, stations[j] - w) and min(n, stations[j]+w) >= i:
            if stations[j] == (i + w):
                print(i)
                i = i + 2*w + 1
            else:
                answer+=1
                i = stations[j] + w + 1
            if j < len(stations)-1:
                j+=1
            elif j == len(stations)-1:
                answer += math.ceil((n - (stations[j]+w))/(2*w+1))
                break
        else:
            answer +=1
            i += 2*w + 1
    return answer
