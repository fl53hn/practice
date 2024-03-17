def solution(n):
    if n < 4:
        n = n % 1234567
        return n
    else:
        a, b = 1, 2
        for i in range(n-2):
            a, b = b, a+b
        return b % 1234567
