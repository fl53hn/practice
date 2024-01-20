def solution(word):
    answer = 0
    words = []
    lan = ['A','E','I','O','U']
    for i in range(len(word)):
        for j in range(len(lan)):
            if word[i] == lan[j]:
                words.append(j)
                continue
        
    print(words)
    for i in range(0, len(words)):
        answer += (781//5**i) * words[i]
    return answer + len(words)
