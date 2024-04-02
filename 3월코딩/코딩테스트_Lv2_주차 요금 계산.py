import math
def solution(fees, records):
    answer = []
    in_out = {}
    parking_fee = {}
    for record in records:
        if record[11] == "I": # 줄이기 위해 11 == I로 함, 실제는 11:12 == IN, else
            in_out[record[6:10]] = record[0:5]
        else:
            if record[6:10] not in parking_fee:
                parking_fee[record[6:10]] = time1(in_out[record[6:10]], record[0:5])
                del in_out[record[6:10]]
            else:
                parking_fee[record[6:10]] += time1(in_out[record[6:10]], record[0:5])
                del in_out[record[6:10]]
    for key in in_out.keys():
        if key not in parking_fee:
            parking_fee[key] = time1(in_out[key], "23:59")
        else:
            parking_fee[key] += time1(in_out[key], "23:59")
    parking_fee = sorted(parking_fee.items())
    print(parking_fee)
    for i in parking_fee:
        answer.append(total_parking_time(fees, i[1]))
    return answer


def time1(in_record, out_record):
    fee1 = (int(out_record[0:2]) - int(in_record[0:2])) * 60 + (int(out_record[3:5]) - int(in_record[3:5]))
    return fee1
    

def total_parking_time(fees, park_time):
    if (int(park_time) - fees[0]) <= 0:
        return fees[1]
    else:
        return fees[1] + math.ceil((int(park_time) - fees[0]) / fees[2]) * fees[3]
# import math

# def solution(fees, records):
#     answer = []
#     dic1 = {}
#     dic2 = {}
#     for i in range(len(records)):
#         if records[i][6:10] not in dic1:
#             dic1[records[i][6:10]] = records[i][0:6]
#         else:
#             a = int(records[i][0:6].split(":")[0]) * 60 + int(records[i][0:6].split(":")[1])
#             b = int(dic1[records[i][6:10]].split(":")[0]) * 60 + int(dic1[records[i][6:10]].split(":")[1])
#             if a-b>fees[0]:
#                 dic2[records[i][6:10]] = fees[1] + math.floor(((a-b) - fees[0]) / fees[2])*fees[3]
#                 del dic1[records[i][6:10]]
#                 print(dic2, dic1,"if")
#             else:
#                 dic2[records[i][6:10]] = fees[1]
#                 del dic1[records[i][6:10]]
#                 print(dic2, dic1,"else")
#     return answer
