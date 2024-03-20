def solution(n, works):
    answer = 0
    k = 0
    works.sort(reverse=True)
    for i in range(n):
        works[k] = works[k] - 1
        if k < len(works)-1:
            if works[k] < works[k+1]:
                k = k+1
            else:
                k = 0
        if k == (len(works)-1):
            if works[k] < 0:
                return 0
            if works[k] < works[k-1]:
                k = 0
    for j in range(len(works)):
        answer += works[j]**2
    return answer

# 힙 사용 다른 사람 풀이
# import heapq # 우선순위 큐(힙) 사용이유:
# # 삽입이나 삭제시 O(log n)으로 자동 정렬되어
# # 최댓값이나 최솟값을 바로 꺼낼 수 있어 빠르다.

# # 파이썬이 제공하는 우선순위 큐(힙) 자료구조는
# # 최소힙이라 최솟값만 구할 수있음

# def solution(n, works):
    
#     # 모든 작업을 처리할 수 있는 경우
#     if sum(works) <= n:
#         return 0

#     # 파이썬이 제공하는 힙 자료구조는 최소힙이므로
#     # 최대힙으로 사용할 수 있게 works를 음수로 변경 후
#     # works를 힙으로 변환
#     works = [-work for work in works]
#     heapq.heapify(works)

#     # n번 동안
#     # 최댓값을 꺼내 1을 더하고(음수로 뒤집었기 때문) 힙에 다시 넣기
#     # (= 최댓값 꺼내서 1빼고 힙에 다시 넣기)와 같음
#     for _ in range(n):
#         work = heapq.heappop(works) + 1
#         heapq.heappush(works, work)

#     # 피로도 계산
#     result = sum([work**2 for work in works])
    
#     return result
