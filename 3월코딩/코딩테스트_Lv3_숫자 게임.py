def solution(A, B):
    answer = 0
    data = 0
    C = []
    A.sort()
    def dfs(A, B, data):
        if data == (len(A)-1):
            return data
        for i in range(len(B)):
            if A[data] < B[i] and B[i] not in C:
                C.append(B[i])
                dfs[A,B,data+1]
            if i == (len(B)-1) and answer == 0:
                return data
    dfs(A,B, data)
    return answer
