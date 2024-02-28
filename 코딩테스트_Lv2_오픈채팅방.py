def solution(record):
    
    answer = []
    nameMap = dict()
    
    for s in record:
        L = s.split()
        
        if L[0] == "Leave":
            continue
            
        nameMap[L[1]] = L[2]
        
    for s in record:
        L=s.split()
        
        if L[0] == "Enter":
            answer.append(nameMap[L[1]] + "님이 들어왔습니다.")
            
        elif L[0] == "Leave":
            answer.append(nameMap[L[1]] + "님이 나갔습니다.")
            
    return answer
# from collections import deque

# def solution(record):
#     answer = deque(record)
#     rec = []
#     for i in range(len(record)):
#         if record[i][0] == "E":
#             rec.append(record[i][7:].split(" "))
#         elif record[i][0] == "L":
#             rec.append(record[i][7:].split(" "))
#         else:         
#     return answer
