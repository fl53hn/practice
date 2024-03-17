def solution(str1, str2):
    answer = 0
    s1,s2 = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha()==True:
            s1.append(str1[i:i+2].lower())

    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha()==True:
            s2.append(str2[j:j+2].lower())
            
    s1_temp = s1.copy()
    hap = s1.copy()

    for i in s2:
        if i not in s1_temp:
            hap.append(i)
        else:
            s1_temp.remove(i)
    
    gyo = []
    
    for i in s2:
	    if i in s1:
                s1.remove(i)
                gyo.append(i)
    
    
    if len(gyo) == 0 and len(hap) == 0:
        answer = 65536
    else:
        print(gyo, hap)
        answer = int(65536 * (len(gyo) / len(hap)))
    
    return answer
