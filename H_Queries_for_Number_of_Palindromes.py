import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

word = cip()
n = ip()

dp = [[0]*n for i in range(n)]
pal = [[False]*n for i in range(n)]
for i in range(n):
    dp[i][i] = 1
    pal[i][i] = True


for i in range(n -1 , -1 , -1):
    for j in range(i +1, n):
        pal[i][j] = pal[i-1][j-1] and word[i] == word[j]
        if i < n-1:
            dp[i][j] = dp[i+1][j-1] 

        dp[i][j] += pal[i][j]
        

for d in dp:
    print(d)