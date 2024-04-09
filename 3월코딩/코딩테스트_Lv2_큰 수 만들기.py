# 출처에 적힌 방식이며, 통과가 가능하지만 필자가 생각한 테스트 케이스에 부합하지 않음
# 입력값 〉	"12321", 3
# 기댓값 〉  "32" --> 실제값 ("321")
# 입력값 〉	"989898", 3
# 기댓값 〉	"999" --> 실제값 ("9998")
#으로 나와 k를 int1에 저장 후 마지막에 뺌
def solution(number, k):
    stack = []
    int1 = k
    for num in number:
        
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1
            
        stack.append(num)
        
    stack = stack[:(len(number)-int1)]
    return ''.join(stack)
#출처: https://1ets-just-do-it.tistory.com/150 [파이썬은 신이야🔥🔥🔥:티스토리]

# # len(number) 있음, k 있음
# # 0 ~ len(number)-k-1 의 값을 max로 리턴 인덱스값 저장
# # 인덱스값 부터 ~ len(number)-k-2 의 값을 max로 리턴, 인덱스 값 저장
# # 반복하면 나옴 else로 인덱스 값부터 len(number) + len(answer) 가 len(number) - k라면 붙이고 return
# def solution(number, k):
#     answer = ''
#     i = 0
#     count = 1
#     while len(answer) != (len(number) - k):
#         num = number[i : k + count]
#         answer+= maxnum(num)[0]
#         i += maxnum(num)[1]+1
#         count +=1 
#         if len(number) - k == len(answer) + len(number[i:len(number)]):
#             answer += number[i:len(number)]
#             break  
#     return answer

#     # while len(answer) != len(number) - k:
#     #     if number[i] < number[i+1]:
#     #         i+=1
#     #     else:
#     #         answer = answer+number[i]
#     #         i+=1
#     #     if len(number) - k == len(answer) + len(number[i:len(number)]):
#     #         answer += number[i:len(number)]
#     #         break
    
    
# def maxnum(number):
#     max1 = number[0]
#     ind = 0
#     if max1 == 9:
#         return [max1, ind]
#     for i in range(len(number)):
#         if number[i] == 9:
#             return[number[i], i]
#             break
#         else:
#             if max1 < number[i]:
#                 max1 = number[i]
#                 ind = i
#     return [max1, ind]
