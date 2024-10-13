import math

def solve():
    n = int(input())
    l, r = 1, 2 * 10**18
    ans = 0
    while l <= r:
        mid = (l + r) // 2
        t = int(math.isqrt(mid))
        
        cnt = mid - t
        if cnt >= n:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    
    print(ans)

t = int(input())
for _ in range(t):
    solve()
