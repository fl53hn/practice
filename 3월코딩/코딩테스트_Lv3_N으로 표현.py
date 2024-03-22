#16:00 시작, 18:45분 포기
def calculate_n(X, Y):
    n_set = set() # set 하나 만들고
    for x in X: # X안에 x 가 있을 때
        for y in Y: # Y안에 y가 있을 때
            n_set.add(x+y) # set에 x + y
            n_set.add(x-y) # set에 x - y
            n_set.add(x*y) # set에 x * y
            if y != 0: # y가 0이 아니라면
                n_set.add(x//y) #x // y
    return n_set #n_set 리턴

def solution(N, number):
    answer = -1 # -1에서 시작
    result = {}   # key는 숫자 사용횟수, value는 숫자를 key번 사용했을 때 나오는 연산 결과셋
    result[1] = {N} # N을 1번 사용할 때는 그냥 N
    if number == N:
        return 1
    for n in range(2, 9):  # 8번까지만 계산하므로
        i = 1
        temp_set = {int(str(N)*n)}  # N=5, 2번 사용할 때 먼저 55를 저장
        # 1 (op) N-1.... n-1 (op) 1 까지 계산
        while i < n:
            temp_set.update(calculate_n(result[i], result[n-i]))
            i += 1
        # 만들어진 셋에 원하는 숫자가 있으면 stop
        if number in temp_set:
            answer = n
            break

        result[n] = temp_set

    return answer

# def solution(N, number):
#     answer = 0
#     # 1. number // N == > N+N ... 1은 N/N으로 표현
#     answer = number//N + (number%N)*2
#     # 2. number // 11 ==> {(10a + a) + 1*a} //a
#     if ((number // 11) * 2 + (number % N) + 1) < answer:
#         answer = (number // 11) * 2 + (number % 11) + 1
#     if (11 * N + N) == number and 3 < answer:
#         answer = 3
#     if (number % (11*N))
#     if answer > 8:
#         return -1
#     return answer

## idea1. 11 // 2사용
## idea2. number // 11 , num % 11 등 사용
