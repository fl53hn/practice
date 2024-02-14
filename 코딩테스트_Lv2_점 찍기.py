def solution(k, d): 
    answer = 0
    a = []
    for i in range(d+1):
        if i*k <= d:
            a.append(i*k)
    for j in a:
        q = d*d - j*j
        answer = answer + (int(q**(1/2)/k)+1)
    return answer
