def solution(s):
    answer = True
    count1 = 0
    for i in range(len(s)):
        if s[i] == "(":
            count1 += 1
        else:
            count1 -= 1 
        if count1 < 0:
            return False
        if i == len(s)-1 and count1 > 0:
            return False
        
    return True
