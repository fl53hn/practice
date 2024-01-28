# def solution(s):
#     answer = -1
#     for i in range(len(s)):
#         if s[0] == ']' or s[0] == ')' or s[0] == '}':
#             continue
#         else:
            
#     return answer

def check(str_list):
    stack = []

    for _str in str_list:
        if _str in ('[', '(', '{'):
            stack.append(_str)
        else:
            if not stack: return False
            x = stack.pop()
            if _str == ']' and x != '[':
                return False
            elif _str == ')' and x != '(':
                return False
            elif _str == '}' and x != '{':
                return False

    if stack: return False
    return True

def solution(s):
    cnt = 0
    for i in range(len(s)):
        u = s[:i]
        v = s[i:]

        if check(v+u):
            cnt +=1
    return cnt
