
MOD = int(1e9 + 7)

def main():
    n, m = map(int, input().split())
    arr  =list( map(int, input().split()))
    dp = [[0] * (m + 1) for _ in range(n)]
    
    x0 = arr[0]
    
    if x0 == 0:
        dp[0] = [1] * (m + 1)
    else:
        dp[0][x0] = 1
    
    for i in range(1, n):
        x = arr[i]

        if x == 0:
            for j in range(1, m + 1):
                for k in (j - 1, j, j + 1):
                    if 1 <= k <= m:
                        dp[i][j] = (dp[i][j] + dp[i - 1][k]) % MOD
        else:
            for k in (x - 1, x, x + 1):
                if 1 <= k <= m:
                    dp[i][x] = (dp[i][x] + dp[i - 1][k]) % MOD

    ans = sum(dp[n - 1][j] for j in range(1, m + 1)) % MOD
    print(ans)

if __name__ == "__main__":
    main()


