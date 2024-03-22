#단짠단짠 알고리즘 LABS 문제
#https://www.youtube.com/watch?v=IlMVmQ7hG4w


n = int(input("개수 입력 : "))
answer = 0
nums = [int(x) for x in input().split()]
nums2 = []

for i in range(len(nums)+1):
    nums2.append(sum(nums[:i]))

dic = {}

for j in range(len(nums2)):
    if not nums2[j] in dic:
        dic[nums2[j]] = 1
    else:
        dic[nums2[j]] +=1

for i in dic:
    answer += (int(dic[i])-1) * (int(dic[i])) // 2


print(answer)