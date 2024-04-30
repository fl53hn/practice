#다익스트라 알고리즘을 떠올렸으나, 연결 확인에서 막힘
def solution(n, costs):
    answer = 0
    costs.sort(key = lambda x: x[2]) # 비용기준으로 오름차순 정렬
    connect = set([costs[0][0]]) # 연결을 확인하는 집합
    
    # Kruskal 알고리즘으로 최소 비용 구하기
    while len(connect) != n:
        for cost in costs:
            if cost[0] in connect and cost[1] in connect:
                continue
            if cost[0] in connect or cost[1] in connect:
                connect.update([cost[0], cost[1]])
                answer += cost[2]
                break
                
    return answer
## 출처: https://soohyun6879.tistory.com/145 [코딩기록:티스토리]
# def solution(n, costs):
#     answer = 0
#     cost = sorted(costs, key = lambda x : (x[2], x[0]))
#     som = []
#     print(cost)
#     if som 
#     return answer
