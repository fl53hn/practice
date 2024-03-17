import heapq 
def solution(n, k, enemy):
    answer = 0
    invinc = [0]*k #무적권

    for i in range(len(enemy)):
        #invinc[0] 랑 비교하면서 invinc 대체
        if enemy[i] > invinc[0]:
            n -= heapq.heapreplace(invinc,enemy[i])
        else:
            n -= enemy[i]
        if n < 0:
            return i
    return len(enemy) #만약 배열이 다 돌고 나서도 여기로 나온다면 n > 0 이라는 뜻으로 무조건 clear

# def solution(n, k, enemy):
#     answer = 0
#     if k == len(enemy):
#         return k
#     else:
#         for i in range(k, len(enemy)):
#             a = enemy[0:i+1]
#             a.sort()
#             for j in range(k):
#                 a.pop()
#             if n<=sum(a):
#                 return i
