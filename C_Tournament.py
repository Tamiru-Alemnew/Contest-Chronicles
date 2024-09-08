import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n , k = tip()
    arr = lip()
    dp = [[0]*(15) for i in range(n+1)]
    for i in range(1 , n+1):
        dp[i][0] = dp[i-1][0] + arr[i-1] - k 

    for i in range(1 , n + 1):
        for j in range(1,min(i+1 , 15)): 

            dp[i][j] = max( dp[i-1][j-1] + arr[i-1]//(2**j) , dp[i-1][j]+ (arr[i-1]//(2**j))-k  )

    print(max(dp[n]))
