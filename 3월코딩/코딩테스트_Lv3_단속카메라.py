def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1]) # routes를 차량이 나간 지점 (진출) 기준으로 정렬
    print(routes)
    camera = -30001 # -30001부터 카메라 위치를 찾습니다.

    for route in routes: # routes 안 하나씩
        if camera < route[0]: # 카메라 최솟값, route[0]보다 작다면
            answer += 1 # answer +=1
            camera = route[1] # 카메라는 앞으로 route[1]
    return answer

# def solution(routes):
#     answer = len(routes)
#     dic1 = {}
#     min = 
#     for i in range(len(routes)):
        
#         # for j in range(routes[i][0], routes[i][1]+1):
#         #     if j not in dic1:
#         #         dic1[j] = 1
#         #     else:
#         #         dic1[j] +=1
#     print(dic1)
#     return answer
