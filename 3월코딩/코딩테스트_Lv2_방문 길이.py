def solution(dirs):
    answer = 0
    place = [0,0]
    dir1 = []
    p0 = place[0]
    p1 = place[1]
    for i in range(len(dirs)):
        if dirs[i] == "U":
            if p1 <= 4:
                if [[p0,p1], [p0,p1+1]] not in dir1 and [[p0,p1+1], [p0,p1]] not in dir1:
                    dir1.append([[p0,p1], [p0, p1+1]])
                p1 = p1 + 1
        elif dirs[i] == "D":
            if p1 >= -4:
                if [[p0,p1], [p0,p1-1]] not in dir1 and [[p0,p1-1], [p0,p1]] not in dir1:
                    dir1.append([[p0,p1], [p0,p1-1]])
                p1 = p1 - 1
        elif dirs[i] == "R":
            if p0 <= +4:
                if [[p0,p1], [p0+1,p1]] not in dir1 and [[p0+1,p1], [p0,p1]] not in dir1:
                    dir1.append([[p0,p1], [p0+1,p1]])
                p0 = p0 + 1
        else:
            if p0 >= -4:
                if [[p0,p1], [p0-1,p1]] not in dir1 and [[p0-1,p1], [p0,p1]] not in dir1:
                    dir1.append([[p0,p1], [p0-1,p1]])
                p0 = p0 - 1
    answer = len(dir1)
    return answer

# def solution(dirs):
#     answer = 0
#     place = [0,0]
#     dir1 = []
#     for i in range(len(dirs)):
#         if dirs[i] == "U":
#             if place[1] <= 4:
#                 if [[place[0],place[1]], [place[0],place[1]+1]] not in dir1 and [[place[0],place[1]+1], [place[0],place[1]]] not in dir1:
#                     dir1.append([[place[0],place[1]], [place[0], place[1]+1]])
#                 place[1] = place[1] + 1
#                 print([place, [place[0], place[1]+1]],"U")
#         elif dirs[i] == "D":
#             if place[1] >= -4:
#                 if [[place[0],place[1]], [place[0],place[1]-1]] not in dir1 and [[place[0],place[1]-1], [place[0],place[1]]] not in dir1:
#                     dir1.append([[place[0],place[1]], [place[0],place[1]-1]])
#                 place[1] = place[1] - 1
#                 print([place, [place[0], place[1]-1]],"D")
#         elif dirs[i] == "R":
#             if place[0] <= +4:
#                 if [[place[0],place[1]], [place[0]+1,place[1]]] not in dir1 and [[place[0]+1,place[1]], [place[0],place[1]]] not in dir1:
#                     dir1.append([[place[0],place[1]], [place[0]+1,place[1]]])
#                 place[0] = place[0] + 1
#                 print([place, [place[0]+1,place[1]]],"R")
#         else:
#             if place[0] >= -4:
#                 if [[place[0],place[1]], [place[0]-1,place[1]]] not in dir1 and [[place[0]-1,place[1]], [place[0],place[1]]] not in dir1:
#                     dir1.append([[place[0],place[1]], [place[0]-1,place[1]]])
#                 place[0] = place[0] - 1
#                 print([place, [place[0]-1,place[1]]],"L")
#     answer = len(dir1)
#     print(dir1)
#     return answer
