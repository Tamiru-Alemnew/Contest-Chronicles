s = input()
n = len(s)
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
	for j in range(n - i):
		dp[j][i + j] = dp[j + 1][i + j] + 1
		for k in range(j + 1, i + j + 1):
			if s[k] == s[j]:
				dp[j][i + j] = min(dp[j][i + j], dp[j + 1][k - 1] + dp[k + 1][i + j])
	for d in dp:
		print(d)
	print(i)

print(dp[0][n - 1])