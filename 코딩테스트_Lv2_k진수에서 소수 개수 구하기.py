import string
tmp = string.digits+string.ascii_lowercase
def solution(n, k):
    answer = 0
    con = convert(n,k).split('0')
    for i in range(len(con)):
        if con[i] == '':
            continue
        else:
            if isPrime(int(con[i])) == True:
                answer+=1
    return answer


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]
    
    
def isPrime(n):
    if n==1:
        return False
    
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
