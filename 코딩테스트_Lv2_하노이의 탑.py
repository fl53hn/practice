def solution(n):
    answer = []
    
    hanoi(n,1,3,2,answer)
    
    return answer


def hanoi(n, from_pos, to_pos, aux_pos, answer):
    if n == 1:  # 원반 한 개를 옮기는 문제면 그냥 옮기면 됨
        answer.append([from_pos,to_pos])
        return

    # 원반 n - 1개를 aux_pos로 이동(to_pos를 보조 기둥으로)
    hanoi(n - 1, from_pos, aux_pos, to_pos, answer)
    # 가장 큰 원반을 목적지로 이동
    answer.append([from_pos,to_pos])
    # aux_pos에 있는 원반 n-1개를 목적지로 이동(from_pos를 보조 기둥으로)
    hanoi(n - 1, aux_pos, to_pos, from_pos, answer)
