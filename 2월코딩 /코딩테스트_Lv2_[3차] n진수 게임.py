def solution(n, t, m, p):
    answer = ''
    game = ''
    cur = p - 1
    for num in range(t * m):
        game += convert(num, n)
    while 1:
        if len(answer) == t:
            break
        answer += game[cur]
        cur += m
    return answer


def convert(number, n):
    if number == 0:
        return '0'
    NUMBERS = "0123456789ABCDEF"
    res = ""
    while number > 0:
        number, mod = divmod(number, n)
        res += NUMBERS[mod]
    return res[::-1]


# import string
# tmp = string.digits+string.ascii_lowercase

# def solution(n, t, m, p):
#     answer = []
#     for i in range(1, t+1):
#         result = (i-1)*m + (p-1)
#         answer.append(convert(result, n))
        
#     return answer


# def convert(num, base) :
#     q, r = divmod(num, base)
#     if q == 0 :
#         return tmp[r] 
#     else :
#         return convert(q, base) + tmp[r]
