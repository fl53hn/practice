def solution(s):
    answer = []
    num = 0
    total = 0
    while True:
        if len(s) == 1:
            break
        num += 1
        count = 0
        for i in range(len(s)):
            if s[i] == "0":
                count += 1
                total += 1
        s = "{0:b}".format(len(s)-count)
    answer.append(num)
    answer.append(total)
    return answer
