import math

def solution(fees, records):
    answer = []
    dic1 = {}
    dic2 = {}
    for i in range(len(records)):
        if records[i][6:10] not in dic1:
            dic1[records[i][6:10]] = records[i][0:6]
        else:
            a = int(records[i][0:6].split(":")[0]) * 60 + int(records[i][0:6].split(":")[1])
            b = int(dic1[records[i][6:10]].split(":")[0]) * 60 + int(dic1[records[i][6:10]].split(":")[1])
            if a-b>fees[0]:
                dic2[records[i][6:10]] = fees[1] + math.floor(((a-b) - fees[0]) / fees[2])*fees[3]
                del dic1[records[i][6:10]]
                print(dic2, dic1,"if")
            else:
                dic2[records[i][6:10]] = fees[1]
                del dic1[records[i][6:10]]
                print(dic2, dic1,"else")
    return answer
