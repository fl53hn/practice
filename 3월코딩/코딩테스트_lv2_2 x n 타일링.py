def solution(n):
    fib=[1,1]
    for i in range(2, n+1):
        fib.append((fib[i-2]+fib[i-1])%1000000007)
    return fib[-1]
