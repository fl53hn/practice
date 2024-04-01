from collections import Counter

def solution(weights):
    answer, counter = 0, Counter(weights)
    print(counter)
    for i in counter:
        if counter[i] > 0:
            answer += counter[i] * (counter[i] - 1) // 2 # nC2 n!/2!(n - 2)!
            answer += counter[i] * counter[i * 3 / 2]
            answer += counter[i] * counter[i * 2]
            answer += counter[i] * counter[i * 4 / 3]

    return answer

# def solution(weights):
#     answer = 0
#     dic2= {}
#     for weight in weights:
#         if weight not in dic2:
#             dic2[weight] = 1
#         else:
#             dic2[weight] += 1
#         if weight * (3/2) not in dic2:
#             dic2[weight*(3/2)] = 0
#         if weight * (2) not in dic2:
#             dic2[weight*(2)] = 0
#         if weight * (4/3) not in dic2:
#             dic2[weight*(4/3)] = 0
    
#     for i in weights:
#         answer += dic2[i] * (dic2[i] - 1) // 2 # nC2 n!/2!(n - 2)!
#         if dic2[i*(3/2)] in dic2:
#             answer += dic2[i] * dic2[i*3/2]
#         if dic2[i*2] in dic2:
#             answer += dic2[i] * dic2[i*2]
#         if dic2[i*(4/3)] in dic2:
#             answer += dic2[i] * dic2[i*4/3]
    
#     return answer


##3번
# def solution(weights):
#     answer = 0
#     weights.sort()
#     dic1 = {}
#     for i in range(0, len(weights)):
#         for j in range(i+1, len(weights)):
#             if weights[i] == weights[j]:
#                 if weights[i] not in dic1:
#                     dic1[weights[i]] = 1
#                 else:
#                     dic1[weights[i]] += 1
#             if weights[i]*1.5 == weights[j]:
#                 if weights[i]*1.5 not in dic1:
#                     dic1[weights[i]*1.5] = 1
#                 else:
#                     dic1[weights[i]*1.5] += 1
#             if weights[i]*2 == weights[j]:
#                 if weights[i]*2 not in dic1:
#                     dic1[weights[i]*2] = 1
#                 else:
#                     dic1[weights[i]*2] += 1
#             if weights[i]*(4/3) == weights[j]:
#                 if weights[i]*(4/3) not in dic1:
#                     dic1[weights[i]*(4/3)] = 1
#                 else:
#                     dic1[weights[i]*(4/3)] += 1
    
#     for i in dic1:
#         answer += int(dic1[i])
#     return answer

## 1번 weights에 있으면 더하기
# def solution(weights):
#     answer = 0
#     for i in range(0,len(weights)):
#         if weights[i] in weights[i+1:len(weights)]:
#             answer+=1
#         if weights[i]*1.5 in weights[i+1:len(weights)]:
#             answer+=1
#         if weights[i]*2 in weights[i+1:len(weights)]:
#             answer+=1
#         if weights[i]*(4/3) in weights[i+1:len(weights)]:
#             answer+=1
#     return answer


## 사전에 넣고 더하기
# def solution(weights):
#     answer = 0
#     dic1 = {}
#     dic2 = {}
#     for weight in weights:
#         if weight not in dic2:
#             dic2[weight] = 1
#         else:
#             dic2[weight] += 1
#     for i in dic2:
#         answer += int(dic2[i])*(int(dic2[i])-1) / 2
    
#     weights = set(weights)
    
#     for weight in weights:
#         if weight not in dic1:
#             dic1[weight] = 1
#         else:
#             dic1[weight] += 1
#         if weight*(3/2) in weights:
#             if weight*(3/2) not in dic1:
#                 dic1[weight*(3/2)] = 1
#             else:
#                 dic1[weight*(3/2)] += 1
#         if weight*(2) in weights:
#             if weight*(2) not in dic1:
#                 dic1[weight*(2)] = 1
#             else:
#                 dic1[weight*(2)] += 1
#         if weight*(4/3) in weights:
#             if weight*(4/3) not in dic1:
#                 dic1[weight*(4/3)] = 1
#             else:
#                 dic1[weight*(4/3)] += 1

#     for i in dic1:
#         answer += int(dic1[i])
    
#     answer -= len(dic1)
#     return answer
