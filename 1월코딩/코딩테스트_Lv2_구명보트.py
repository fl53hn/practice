def solution(people, limit):
    people.sort()
    count=0
    
    front, end = 0, len(people)-1
    
    while end>=front:
        if people[front] + people[end]<=limit:
            front+=1
        end -=1
        count += 1
    return count

#def solution(people, limit):
#    answer = 0
#    people.sort(reverse=True)
#    while people:
#        if len(people) > 1 and limit >= people[-1] + people[-2]:
#            people.pop()
#            people.pop()
#            answer += 1
#            continue
#        else:
#            answer += len(people)
#            return answer
#            break
