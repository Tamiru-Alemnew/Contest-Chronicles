def solve():
    n, k = map(int, input().split())
    
    has = {}
    
    for i in range(n):
        for j in range(k):
            num = int(input())
            if num not in has:
                has[num] = [j, j]
            else:
                has[num][0] = min(has[num][0], j)
                has[num][1] = max(has[num][1], j)
    
    dp = [0] * (k + 1)
    
    for i in range(k - 1, -1, -1):
        dp[i] = dp[i + 1]
        for j in range(1, k + 1):
            if j in has and has[j][0] == i:
                dp[i] = max(dp[i], dp[has[j][1]] + 1)
    
    mx = max(dp)
    cnt = sum(1 for i in range(k) if dp[i] == mx)
    
    print(mx, cnt)

if __name__ == "__main__":
    solve()
