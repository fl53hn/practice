def solution(m, n, puddles):
    dp = [[0] * (m+1) for a in range(n+1)]
    dp[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles or [i,j] == [1,1]:
                continue
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return (dp[-1][-1] % 1000000007)

# 이건 DFS인데 왜 DP라고 적었지
# def solution(m, n, puddles):
#     answer = 0
#     def dp(m, n, puddles):
#         if [m, n] == [1, 1]:
#             nonlocal answer
#             answer= (answer + 1)%1000000007 
#         else:
#             if not [m-1, n] in puddles and m>1:
#                 dp(m-1, n, puddles)
#             if not [m, n-1] in puddles and n>1:
#                 dp(m, n-1, puddles)
    
#     dp(m, n, puddles)
    
#     return answer%1000000007
