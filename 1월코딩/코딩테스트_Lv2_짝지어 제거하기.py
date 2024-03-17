def solution(s):
    stack = []
    for i in range(len(s)):
        if not stack:
            stack.append(s[i])          
        else:
            if s[i] == stack[-1]:       
                stack.pop()
            else:
                stack.append(s[i])      

    if stack:
        return 0                 
    else:
        return 1


#def solution(s):
#    while len(s) != 0:
#        if len(s)%2 != 0:
#            return 0
#            break
#        for i in range(len(s)):
#            if i != len(s)-1 and s[i] == s[i+1]:
#                s = s.replace(s[i], '', 2)
#                break
#            if i == len(s)-1:
#                return 0
#                break
#    if len(s) == 0:
#        return 1
