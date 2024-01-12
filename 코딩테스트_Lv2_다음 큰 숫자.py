def solution(n):
    answer = 0
    one_count = bin(n).count("1")
        
    for j in range(n+1,1000001):
        one_count2 = bin(j).count("1")
        if one_count2 == one_count:
            return j
