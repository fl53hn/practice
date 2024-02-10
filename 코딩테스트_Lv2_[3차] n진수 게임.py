import string
tmp = string.digits+string.ascii_lowercase

def solution(n, t, m, p):
    answer = []
    for i in range(1, t+1):
        result = (i-1)*m + (p-1)
        answer.append(convert(result, n))
        
    return answer


def convert(num, base) :
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r] 
    else :
        return convert(q, base) + tmp[r]
