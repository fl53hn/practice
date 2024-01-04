def solution(s):
    answer = []
    for i in range(len(s.split(' '))):
        answer.append(int(s.split(' ')[i]))
    a = ""
    b = min(answer)
    c = max(answer)
    a = str(b) + " " + str(c)
    return a
