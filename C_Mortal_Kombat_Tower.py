import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;
"""
    1 0 1 1 0 1 1 1
    
0 0 1 1 2 3 
1 0 1 1 2 3


"""
for i in range(ip()):
    n = ip()
    dp = [[inf]*(n+1) for i in range(2)]

    arr = lip()

    dp[0][0] = 0

    for i in range(n):
        dp[1][i+1]  = min(dp[1][i+1], dp[0][i] + arr[i])
        dp[0][i+1] = min(dp[0][i+1], dp[1][i] )

        if i + 2 < n+1 :
            dp[1][i+2] = min(dp[1][i+2], dp[0][i] + arr[i] + arr[i+1])
            dp[0][i+2] = min(dp[0][i+2], dp[1][i])

    print(min(dp[0][n] , dp[1][n]))
