n , s = map(int, input().split())
arr = list(map(int, input().split()))
cur = 0
ans = float("inf")
l = 0

for r in range(n):
    cur += arr[r]
    
    while cur >= s :
        ans = min(ans , r - l +1)
        cur -= arr[l]
        l += 1

print(-1 if ans == float("inf") else ans)