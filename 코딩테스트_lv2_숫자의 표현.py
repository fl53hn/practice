def solution(n):
    answer = 0
    num = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            num += j
            if num == n:
                answer += 1
                num = 0
                break
            if num > n:
                num = 0
                break
    return answer
