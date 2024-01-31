def solution(citations):
    citations.sort(reverse=True)
    answer=0
    n = len(citations)
    for i in range(n-1, -1, -1):
        if citations[i]>=i+1:
            return i+1
    return answer
