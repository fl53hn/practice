def solution(msg):
    answer = []
    dic1 = {}
    word = ''
    count = 0
    AZ = ["A","B","C","D","E","F","G","H","I","J","K",
          'L','M','N','O','P','Q','R','S','T','U',"V",'W','X','Y','Z']
    for i in range(len(AZ)):
        dic1[AZ[i]] = i+1

    while count < len(msg):
        word += msg[count]
        if word in dic1:
            count +=1
            if count == (len(msg)):
                answer.append(dic1[word])
        else:
            answer.append(dic1[word[0:(len(word)-1)]])
            dic1[word] = int(len(dic1)+1)
            word = ''

    return answer
