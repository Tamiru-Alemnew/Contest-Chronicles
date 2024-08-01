n = int(input())

dp = [0]*(n + 1)

for i in range(1 , min(n +1 , 7)):
    dp[i] = 1

for i in range(2 , n+1):
    for j in range(1 , min(i , 7)):
        dp[i] += dp[i- j]

print(dp[n]%(10**9+7))

