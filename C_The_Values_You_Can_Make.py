
def main():
    n, k = map(int, input().split())
    
    dp = [[[False for _ in range(k + 1)] for _ in range(k + 1)] for _ in range(2)]

    arr = list(map(int, input().split()))
               
    dp[0][0][0] = True
    
    for i in range(1, n + 1):
        now = i % 2
        last = 1 - now
        
        x =  arr[i-1]
        
        for j in range(k + 1):
            for y in range(j + 1):
                dp[now][j][y] = dp[last][j][y]
                
                if j >= x:
                    dp[now][j][y] |= dp[last][j - x][y]
                    
                    if y >= x:
                        dp[now][j][y] |= dp[last][j - x][y - x]
    

    res = []
    
    for i in range(k + 1):
        if dp[n % 2][k][i]:
            res.append(i)
    
    print(len(res))
    print(' '.join(map(str, res)))

if __name__ == "__main__":
    main()

