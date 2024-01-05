def solution(s):
    answer = ''
    print(len(s))
    for i in range(0, len(s)):
        if i == 0 or len(s)>i and s[i-1] == ' ':
            answer = answer + s[i].upper()
        else:
            answer = answer + s[i].lower()
    return answer
