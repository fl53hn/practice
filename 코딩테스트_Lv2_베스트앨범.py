def solution(genres, plays):
    answer = []
    sumdict = {}
    hashdict = {}
    for i in range(len(plays)):
        if genres[i] in sumdict:
            sumdict[genres[i]] += plays[i]
        else:
            sumdict[genres[i]] = plays[i]
    
    for j in range(len(plays)):
        hashdict[plays[j]] = genres[j]
    
    print(hashdict)
    
    print(sorted(hashdict.items(),reverse=True))
    
    
    print(sorted(sumdict.items(),reverse=True))
    
    return answer
