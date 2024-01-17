def solution(n, words):
    answer = []
    n_words = []
    for i in range(len(words)):
        if words[i] in n_words:
            answer.append((i % n) + 1)
            answer.append((i//n)+1)
            return answer
            break
        else:
            n_words.append(words[i])
        if 0 < i:
            if words[i][0] != words[i-1][-1] or len(words[i]) == 1:
                answer.append((i % n) + 1)
                answer.append((i//n)+1)
                return answer
                break
        else:
            if len(words[i]) == 1:
                answer.append((i % n) + 1)
                answer.append((i//n)+1)
                return answer
                break
        if i == len(words)-1:
            return[0,0]
