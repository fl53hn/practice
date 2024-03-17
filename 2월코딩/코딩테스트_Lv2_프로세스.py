# def solution(priorities, location):
#     answer = 0
#     dr = 0
#     dic = {}
#     loc = []
#     while priorities:
#         max1 = priorities[0]
#         for i in range(len(priorities)):
#             if max1 < priorities[i]:
#                 max1 = priorities[i]
#         priorities.pop(max1)
#     dic[dr] = max1
#     print(dic)
#     return answer
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
