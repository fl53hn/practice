from collections import deque
def solution(A,B):
    answer = 0
    A.sort()
    B.sort()
    A = deque(A)
    B = deque(B)
    while B:
        if A[0] < B[0]:
            A.popleft()
            B.popleft()
            answer+=1
        else:
            B.popleft()
    return answer

### 사용은 가능하나 시간복잡도에서 밀림
# def solution(A, B):
#     answer = 0
#     data = 0
#     A.sort()
#     B.sort()
#     def dfs(A, B, data1, data2):
#         nonlocal answer
#         if data1 == (len(A)) or data2 == (len(B)):
#             return answer
#         if A[data1] < B[data2]:
#             answer+=1
#             return dfs(A, B, data1+1, data2+1)
#         else:
#             return dfs(A, B, data1, data2+1)

#     return dfs(A, B, 0, 0)

# def solution(A, B):
#     answer = 0
#     data = 0
#     C = []
#     A.sort()
#     def dfs(A, B, data):
#         if data == (len(A)-1):
#             return len(C)
#         for i in range(len(B)):
#             if A[data] < B[i] and B[i] not in C:
#                 C.append(B[i])
#                 dfs(A,B,data+1)
#             if i == (len(B)-1) and answer == 0:
#                 return len(C)
#     return dfs(A,B,data)
