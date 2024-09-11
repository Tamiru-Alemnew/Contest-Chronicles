import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

grid = []
mod = 10**9+7
for _ in range(ip()):
    grid.append(cip())

dp = [[0]*(len(grid) + 1) for i in range(len(grid)+1)]


dp[1][1] = 1

for i in range(1 , len(dp) ):
    for j in range(1 , len(dp)):
        if grid[i-1][j-1] != "*":

            dp[i][j] +=( dp[i-1][j] + dp[i][j-1])%mod

print(dp[-1][-1]%mod)