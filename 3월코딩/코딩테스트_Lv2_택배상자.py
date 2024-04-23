from collections import deque  
def solution(order):  
    answer = 1  
    order = deque(order)  
    stack = []  
    result = []  
    size = len(order)  
    for i in range(1, size + 1):  
        stack.append(i)  #박스를 서브 컨테이너에 옮긴다
        while stack:  
            if order and stack[-1] == order[0]:  #서브 컨테이너에서 트럭으로 옮긴다
                num = stack.pop()  
                order.popleft()  
                result.append(num)  
            else:  #만약 트럭으로 옮기는 순서가 잘못 됐다면 중지한다.
                break  
    return len(result) #트럭에 실은 박스 갯수를 반환한다.
# from collections import deque
# def solution(order):
#     answer = 0
#     deque1 = deque()
#     for i in range(len(order)):
#         if i == (len(order)-1):
#             if (order[i]) == order[i-1]-1:
#                 deque1.append(order[i])
#         else:
#             if (order[i] - 1) == order[i+1]:
#                 deque1.append(order[i])
        
#     answer = len(deque1)
#     print(deque1)
#     return answer
