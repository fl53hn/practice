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

######
def solution(k, dungeons):
    Visited = [0 for i in range(len(dungeons))]
    an = []
    for i in range(len(dungeons)):
        Visited = [0 for i in range(len(dungeons))]
        an.append(dfs(i, k, dungeons, Visited))
        print("hh")

        
def dfs(i, k, dungeons, Visited):
    answer = 0
    print(Visited)
    for j in range(len(dungeons)):
        if not Visited[i] == 1:
            if k >= dungeons[i][0]:
                Visited[i] = 1
                k = k - dungeons[i][1]
                answer += 1
                dfs(j, k, dungeons, Visited)
            else:
                continue
        else:
            continue
    return answer
        
        
