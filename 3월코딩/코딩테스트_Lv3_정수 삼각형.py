def solution(triangle):

    floor = len(triangle) - 1  # N층의 인덱스

    while floor > 0:  # N, N-1,...2, 1
        for i in range(floor):  # N번째 인덱스엔 0~N-> N+1개의 숫자가 있음
            # 바로 위층의 칸에 아래칸의 두개중 큰값을 더해줌
            triangle[floor-1][i] += max(triangle[floor][i], triangle[floor][i+1])
        floor -= 1  # 층하나 올라가기

    return triangle[0][0]

# def solution(triangle):
#     answer = 0
#     for i in range(1, len(triangle)):
#         for j in range(len(triangle[i])):
#             if j == 0:	# 왼쪽 끝이면
#                 triangle[i][j] += triangle[i-1][0]  # 이전 층의 0번째 값 더하기
#             elif j == len(triangle[i])-1:	# 오른쪽 끝이면
#                 triangle[i][j] += triangle[i-1][-1]	# 이전 층의 -1번째 값 더하기
#             else:
#                 triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])

#     return max(triangle[-1])

## def solution(triangle):
##     s = 0
##     def dfs(triangle, hei, tri, answer):
##         if hei == (len(triangle)):
##             nonlocal s
##             if answer>s:
##                 s = answer
##             return
##         else:
##             dfs(triangle, hei+1, tri, answer+triangle[hei][tri])
##             dfs(triangle, hei+1, tri+1, answer+triangle[hei][tri])
##     dfs(triangle, 0, 0, 0)
##     return s
