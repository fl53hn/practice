from itertools import permutations as pm
def solution(numbers):
    pm_results = set()
    for i in range(1, len(numbers) + 1):
        i_result = pm(numbers, i) # numbers에서 i개 뽑은 결과
        for r in i_result:
            pm_results.add(int(''.join(r)))
    # 최댓값 범위 내에서 소수 찾기
    max_num = max(pm_results)
    for i in range(2, int(max_num**(1/2)) + 1): # i의 배수들 제거하기
        temp_s = {i * j for j in range(2, max_num//i + 1)}
        pm_results -= temp_s
        pm_results -= {0, 1} # 0과 1은 소수가 아니므로 제거한다.
    return len(pm_results)

# def solution(numbers):
#     answer = 0
#     aq = [int(a) for a in str(numbers)]
#     print(aq)
#     return answer


# def isPrime(num):
#     if num == 2 or num == 3 or num == 5:
#         return num
#     for i in range(2, num//2):
#         if num % i == 0:
#             break
#         if i== (num//2)-1:
#             return num
