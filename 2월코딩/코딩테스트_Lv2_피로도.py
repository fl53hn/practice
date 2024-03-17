answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    # 최대 방문 횟수 초기화
    if cnt > answer:
        answer = cnt
        # 방문 시작 점 설정
        # DFS로 탐색이 끝나고, 다른 시작 점으로 탐색 시작
    for j in range(N):
            # 피로도가 충분해서 방문할 수 있지만, 아직 방문하지 않은 경우
        if k >= dungeons[j][0] and not visited[j]:
                # 방문 처리
            visited[j] = 1
                # 줄어든 피로도로 던전 방문 시작
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
                # 해당 순서로 던전을 모두 방문했으니, 다시 초기화
            visited[j] = 0
                
                
def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    return answer


##################################################

# def solution(k, dungeons):    
#     Visited = [0 for i in range(len(dungeons))]
    
#     for i in range(len(dungeons)):
#         dfs(dungeons,i, k, Visited)
#     return answer

# def dfs(dungeons, i, k, Visited):
#     answer = 0
#     for i in range(len(dungeons)):
#         if k >= dungeons[i][0]:
#             Visited[i] = True
#             answer+=1
#             k -= dungeons[i][1]
#             if not Visited[i]:
#                 dfs(graph, k, Visited)

#########################################
# def solution(k, dungeons):
#     Visited = [0 for i in range(len(dungeons))]
#     an = []
#     for i in range(len(dungeons)):
#         Visited = [0 for i in range(len(dungeons))]
#         an.append(dfs(i, k, dungeons, Visited))
#         print("hh")

        
# def dfs(i, k, dungeons, Visited):
#     answer = 0
#     print(Visited)
#     for j in range(len(dungeons)):
#         if not Visited[i] == 1:
#             if k >= dungeons[i][0]:
#                 Visited[i] = 1
#                 k = k - dungeons[i][1]
#                 answer += 1
#                 dfs(j, k, dungeons, Visited)
#             else:
#                 continue
#         else:
#             continue
        
