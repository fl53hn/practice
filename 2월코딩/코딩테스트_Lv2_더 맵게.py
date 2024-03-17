import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0]<K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)
        heapq.heappush(scoville, mix)
        answer+=1
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        
    return answer

# from collections import deque
# def solution(scoville, K):
#     answer = 0
#     sco = 0
#     scoville.sort()
#     for i in range(0, len(scoville)):
#         if K<sco and K< scoville[i]:
#             return answer
#         elif sco ==0:
#             sco = (scoville[i] + scoville[i+1]*2)
#             answer+=1
#         else:
#             if sco < scoville[i+1]:
#                 sco = sco + scoville[i+1]*2
#                 answer +=1
#             else:
#                 sco = scoville[i+1] + sco*2
#                 answer +=1
#         if i == (len(scoville)-1):
#             return -1
