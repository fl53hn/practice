def solution(n):
    result = ""
    while (n > 0):
        n -= 1
        result = "124"[n%3] + result
        n //= 3
    return result

# def solution(n):
#     answer = ''
#     while n!=0:
#         if n%3 == 0:
#             answer= answer + '4'
#             n = n // 3 - 1
#         elif n%3 == 1:
#             answer = answer + '1'
#             n = n // 3
#         elif n%3 == 2:
#             answer = answer + '2'
#             n = n // 3
#     return answer
