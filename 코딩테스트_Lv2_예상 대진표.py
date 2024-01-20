def solution(n,a,b):
    answer = 1
    a=a-1
    b=b-1
    while a//2!=b//2:
        a=a//2
        b=b//2
        answer+=1
    return answer

# def solution(n,a,b):
#     answer = 0
#     if a % 2 != 0:
#         a = a + 1
#     if b % 2 != 0:
#         b = b + 1
        
    
    
    
#     if a>b:
#         answer = (a-b) // 2 + 1
#     else:
#         answer = (b-a) // 2 + 1
        
#     return answer


# def solution(n,a,b):
#     answer = 0
#     if a > b:
#         answer = b
#         b = a
#         a = answer
#         answer = 0
#     if a % 2 != 0 and b-a == 1:
#         return 1
#     n = n // 2
#     if n < b and n >= a:
#         answer = len(bin(n))-2
#         return answer
#     elif n < a:
#         print(3*n, a, b)
#         return solution(3*n, a, b) - 1
#     else:
#         print(n, a, b)
#        return solution(n, a, b)
