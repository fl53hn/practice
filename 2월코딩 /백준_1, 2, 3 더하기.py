def solution(n):
    answer = 0
    def dfs(result):
        if result==n:
            nonlocal answer
            answer+=1
            return 0
        if result>n:
            return 0
        else:
            dfs(result+1)
            dfs(result+2)
            dfs(result+3)
    dfs(0)
    return answer
