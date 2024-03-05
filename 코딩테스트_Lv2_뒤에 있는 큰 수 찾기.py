def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
            while stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            stack.append(i)
    
    return answer

# def solution(numbers):
#     answer = []
#     max1 = 0
#     count = 0
#     for i in range(len(numbers)):
#         if max1 >= numbers[i]:
#             count+=1
#         else:#max < numbers[i]
#             if numbers[i] == max(numbers) or i == len(numbers)-1:
#                 answer.append(-1)
#                 max1 = 0
#             else:
#                 if max1 != 0:
#                     for j in range(0, count+1):
#                         answer.append(max1)
#                         print(max1, "왜?")
#                 else:
#                     max1 = numbers[i]
#             count = 0
#     return answer
