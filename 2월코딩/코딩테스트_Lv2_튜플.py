def solution(s):
    answer = []
    s = s[2:len(s)-2].split('},{')
    s = sorted(s, key=len)
    for i in range(0,len(s)):
        s1 = s[i].split(",")
        for j in range(0,len(s1)):
            if int(s1[j]) not in answer:
                answer.append(int(s1[j]))
    return answer
