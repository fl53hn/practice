# math에 factorial 있었네...
import math
def solution(n, k):
    arr = [i for i in range(1, n + 1)]
    answer = []

    while arr:
        a = (k - 1) // math.factorial(n - 1)
        answer.append(arr.pop(a))
        
        k = k % math.factorial(n - 1)
        n -= 1
    
    return answer


# from collections import deque
# def solution(n, k):
#     answer = []
#     ans = [i for i in range(1,n+1)]
#     ans = deque(ans)
#     an = deque(factorial(n))
#     for i in range(len(an)-1, -1, -1):
#         answer.append(ans.pop(((k-1)//an[i]) +1))
#         k = k % an[i] +1
#     #answer.append(ans.popleft(an[-2]//n))
#     # print(k // an.pop())
#     # print(an[-2])
#     return answer


# def factorial(n):
#     ans = []
#     j = 1
#     for i in range(1, n):
#         j *=i
#         ans.append(j)
#     return ans

    
# #0~5 n // k 가 0이면 n이 4x3x2x1 (k-1) // i == 0
# 1234
# 1243
# 1324
# 1342
# 1423
# 1432
# #7~12 n // k 가 1이면
# 2134
# 2143
# 2314
# 2341
# 2413
# 2431
# #13~18
# 3
# 3
# 3
# 3
# 3
# 3
# #19~24 # (k-1//i) +1
# 4
# 4
# 4
# 4
# 4
# 4
