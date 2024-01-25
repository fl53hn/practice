def solution(k, tangerine):
    answer = 0
    a={}
    for i in tangerine:
        if i in a: #a 안에 i 가 있으면
            a[i]+=1 #a[i]에 갯수 +1
        else:
            a[i]=1 #없으면 a[i]가 1부터 시작
    a = dict(sorted(a.items(), key=lambda x: x[1], reverse=True)) #a값 정렬
    for i in a:
        if k<=0:
            return answer
        k-=a[i] #하나씩 빼기
        answer+=1
    return answer

# def solution(k, tangerine):
#     count = 0
#     while len(tangerine) != 0:
#         count +=1
#         if k % len(tangerine)==0:
#             return len(set(tangerine))
#         for i, a in enumerate(set(tangerine)):
#             tangerine.remove(a)
#         if i == 0: return a
