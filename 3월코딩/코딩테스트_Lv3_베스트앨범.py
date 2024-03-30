## dic1과 dic2 로 나눔
## dic1은 장르와 고유번호, 플레이 횟수 저장, dic2는 총 플레이 횟수 저장
## sort 후 answer return
## https://velog.io/@sem/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-LEVEL3-%EB%B2%A0%EC%8A%A4%ED%8A%B8%EC%95%A8%EB%B2%94-Python
def solution(genres, plays):
    answer = []
    dic1 = {}
    dic2 = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
            
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)

    return answer

    
    return answer

# def solution(genres, plays):
#     answer = []
#     dic = {}
    
#     for i in range(len(genres)):
#         if genres[i] not in dic:
#             dic[genres[i]] = [plays[i],i]
#         else:
#             dic[genres[i]][0] += plays[i]
#     print(dic)
#     return answer
