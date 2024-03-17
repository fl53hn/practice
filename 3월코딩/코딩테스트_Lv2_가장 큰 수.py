def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    numbers.sort(key=lambda x:x*4, reverse=True)
    answer=str(int(''.join(numbers)))

    return answer

# def solution(numbers):
#     answer = ''
#     ans = ''
#     V = []
#     Visited = [0 for i in range(len(numbers))]
#     for i in range(len(numbers)):
#         V.append(dfs(numbers, i, Visited, ans))
#     return answer


# def dfs(num, v, Visited,ans):
#     Visited[v] = True
#     ans = ans + str(num[v])
    
#     for i in num[v]:
#         if not Visited[i]:
#             dfs(num, i, visited,ans)

#     return ans


    # num = sorted(numbers, key=lambda x: (str(x)[0], len(str(x))), reverse=True)
    # for i in range(len(num)):
    #     answer= answer + str(num[i])
