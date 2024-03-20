def solution(n, s):
    answer = []
    if n > s:
        return [-1]
    elif n == s:
        return [1 for i in range(n)]
    else:
        if s % n == 0:
            return [s//n for i in range(n)]
        else:
            answer = [s//n for i in range(n)]
            s = s - (s//n * n)
            print(s)
            for i in range(s):
                answer[-1 -i] = answer[-1 -i]+1
            return answer
