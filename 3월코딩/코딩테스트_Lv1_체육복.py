# 그리디 알고리즘 공부

def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    answer = n

    #여분이 있는데 도난당한 경우
    reserve_and_lost = lost_set & reserve_set
    lost_set -= reserve_and_lost
    reserve_set -= reserve_and_lost

    for x in reserve_set:
        if x-1 in lost_set:
            lost_set.remove(x-1)
        elif x+1 in lost_set:
            lost_set.remove(x+1)

    answer -= len(lost_set)
    return answer

# def solution(n, lost, reserve):
#     answer = 0
#     re_set = set()
#     for i in reserve:
#         if i not in lost:
#             if i-1 in lost and i-1 not in reserve:
#                 re_set.add(int(i)-1)
#             elif i+1 in lost and i+1 not in reserve:
#                 re_set.add(int(i)+1)
#         else:
#             re_set.add(int(i))
#     print(re_set)
#     if len(re_set)>len(reserve):
#         answer = n - len(lost) + len(reserve)
#     else:
#         answer = n - len(lost) + len(re_set)
#     return answer
