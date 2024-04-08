import math
def solution(n, stations, w):
    answer = 0
    V = [0 for station in range(len(stations)+1)]
    title = 1
    
    for i in range(0, len(stations)):
        if stations[i] - w > 1:
            V[i] = stations[i] - w - title
            title = stations[i] + w + 1
        else:
            title = stations[i] + w + 1
    if n-title+1 > 0:
        V[-1] = n - title + 1
        
    for i in range(len(V)):
        answer+=math.ceil(V[i]/(2*w+1))
    
    return answer



# # 밑에 방식 말고 dic에 -w ~ +w 형식으로 저장 후, 남은 배열 추출. 추출된 배열 % 2w+1 해서 구하기
# def solution(n, stations, w):
#     answer,i = 0,1
#     array = []
#     dic = {}
#     for station in stations:
#         dic[int(station-w)] = int(station+w)
#     # for i in range(len(dic)):
#     #     # dic[i] == 5
#     #     # dic[]
#     print(dic)
#     for d in dic:
#         print(d-i)
#         array.append(d - i)
#         i += dic[d]
#         print(i,"2")

#     print(array)
#     return answer

# import math
# # 1. 그리디?
# # N: 200,000,000
# # 1 ~ (2*w)+1 설치, 6~10 사이 있음, 
# def solution(n, stations, w):
#     i,j = 1, 0
#     answer = 0
#     while i <= n:
#         if (i + (2*w)) >= (stations[j] - w) and (stations[j]+w) >= i:
#             if stations[j] == (i + w):
#                 print(i)
#                 i = i + 2*w + 1
#             else:
#                 if stations[j] > 2*w:
#                     answer+=1
#                 i = stations[j] + w + 1
#             if j < len(stations)-1:
#                 j+=1
#             elif j == len(stations)-1:
#                 answer += math.ceil((n - (stations[j]+w))/(2*w+1))
#                 break
#         else:
#             answer +=1
#             i += 2*w + 1
#     return answer
