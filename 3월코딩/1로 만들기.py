a = int(input())

dp = [0,0,1,1]

for i in range(4, a+1):
    dp.append(dp[i-1]+1)
    print(dp, i, "append")
    if i%2 == 0:
        dp[i] = min(dp[i//2]+1, dp[i])
        print(dp, i, "%2")
    if i%3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
        print(dp, i, "%3")

print(dp[a])
