import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
s = n*(n+1)// 2

if not even(s) :
    print(0)
    exit(0)
mod = 10**9+7
dp = [[0]*(s+1) for i in range(n+1)]

dp[0][0] = 1

for i in range(1 , n +1):
    for j in range(1 , s + 1):
        dp[i][j] += dp[i-1][j]
        dp[i][j] %= mod
        
        if j - i >= 0:
            dp[i][j] += dp[i-1][j-i]
            dp[i][j] %= mod

ans = 0 

ans += sum(dp[n][i] for i in range(s) if i == s//2)

print(ans)