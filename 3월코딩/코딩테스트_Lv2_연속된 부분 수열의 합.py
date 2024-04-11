#https://school.programmers.co.kr/questions/46973
def solution(sequence, k):
    n = len(sequence)

    max_sum = 0
    end = 0

    res = []
    for i in range(n):

        while max_sum < k and end < n:
            max_sum += sequence[end]
            end += 1

        if max_sum == k:
            res.append([i, end-1, end-1-i])

        max_sum -= sequence[i]

    res = sorted(res, key=lambda x: x[2])
    return res[0][:2]

# def solution(sequence, k):
#     answer = []
#     seq = []
#     dic = {}
#     sum = 0
#     for i in range(len(sequence)):
#         seq.append(sum)
#         sum += sequence[i]
#     seq.append(sum)
           
    
#     for j in range(0,len(seq)-1):
#         for q in range(j+1, len(seq)):
#             if seq[q] - seq[j] == k:
#                 if q-j-1 not in dic:
#                     dic[q-j-1] = [j, q-1]

#     return dic[min(dic.keys())]
