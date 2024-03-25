from collections import deque
# deque 사용법
# queue == FIFO
# deque(iterable, [maxlen]) 초기화
# append(x), popleft(), clear() 삽입, 삭제 후 리턴, 원소 지우기
def solution(operations):
    answer = []
    deque1 = deque()
    for i in range(0, len(operations)):
        if operations[i][0] == "I": # 삽입
            deque1.append(int(operations[i][2:]))
        elif operations[i][0:3] == "D 1": # 최댓값 삭제
            if len(deque1) != 0: # deque가 비어있으면 무시
                deque1.remove(max(deque1))
        else: #최솟값 삭제
            if len(deque1) != 0: # deque가 비어있으면 무시
                deque1.remove(min(deque1))
        if i == (len(operations)-1): #끝까지 왔을 때
            if len(deque1) == 0: #비어있으면 [0,0 리턴]
                return [0,0]
            else: # max, min 리턴
                answer.append(max(deque1))
                answer.append(min(deque1))
                return answer
