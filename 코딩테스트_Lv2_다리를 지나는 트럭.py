from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight = 0
    while len(truck_weights)!=0:
        answer+=1
        
        currentWeight -= bridge.popleft()
        
        if currentWeight + truck_weights[0] <= weight:
            currentWeight+=truck_weights[0]
            bridge.append(truck_weights.popleft())
            
        else:
            bridge.append(0)
            
    answer += bridge_length
    return answer


# from collections import deque
# def solution(bridge_length, weight, truck_weights):

#     answer = 0
#     queue = [(0,p) for p in truck_weights]
#     cur = []

#     while queue:
#         if (weight>=cur[1] + q[1] for q in queue) and bridge_length>= len(cur):
#             for i in range(len(cur)):
#                 cur[i][0]+1
#             cur.append(queue.pop(0))
#         else:
#             for i in range(len(cur)):
#                 cur[i][0] + 1
#         if cur[0][0] == bridge_length:
#             answer += cur[0][0] 
#             cur.pop(0)
#     return answer
