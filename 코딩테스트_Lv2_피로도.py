def solution(k, dungeons):    
    Visited = [0 for i in range(len(dungeons))]
    
    for i in range(len(dungeons)):
        dfs(dungeons,i, k, Visited)
    return answer

def dfs(dungeons, i, k, Visited):
    answer = 0
    for i in range(len(dungeons)):
        if k >= dungeons[i][0]:
            Visited[i] = True
            answer+=1
            k -= dungeons[i][1]
            if not Visited[i]:
                dfs(graph, k, Visited)
