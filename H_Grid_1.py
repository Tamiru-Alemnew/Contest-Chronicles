import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

h , w = tip()
grid = []

for  i in range(h):
    grid.append(cip())


dp = [[0]*(w+1) for i in range(h+1)]
dp[0][0] = 1
for r in range(h):
    for c in range(w):
        if grid[r][c] == ".":
            dp[r+1][c] += dp[r][c] 
            dp[r][c+1] += dp[r][c] 


mod = 10**9 + 7

print((dp[h-1][w-1])%mod) 