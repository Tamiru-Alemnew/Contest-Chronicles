import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


with open('hps.in', 'r') as file:
    # Read the first line and parse n and k
    n, k = map(int, file.readline().strip().split())
    
    # Initialize an empty list to store Bessie's gestures
    Bessie = []
    
    # Read the next n lines for Bessie's gestures
    for i in range(n):
        Bessie.append(file.readline().strip())


dp = [[[0 for cur in range(3)] for i in range(k+2)] for j in range(n+1)]

for i in range(1, n+1):

    for j in range(min(i+1 , k+1)):

        if Bessie[i-1] == "H":
            dp[i][j][0] = max(dp[i][j][0] ,dp[i-1][j][0] , max(dp[i-1][j-1][1] , dp[i-1][j-1][2]))
            dp[i][j][1] = max(dp[i][j][1] ,dp[i-1][j][1] , max(dp[i-1][j-1][0] , dp[i-1][j-1][2]))

            dp[i][j][2] = max(dp[i][j][2] ,dp[i-1][j][2] + 1 , max(dp[i-1][j-1][0] , dp[i-1][j-1][1]) +1 )

        if Bessie[i-1] == "S":
            dp[i][j][0] = max(dp[i][j][0] ,dp[i-1][j][0]  + 1  , max(dp[i-1][j-1][1] , dp[i-1][j-1][2])  + 1 )

            dp[i][j][1] = max(dp[i][j][1] ,dp[i-1][j][1] , max(dp[i-1][j-1][0] , dp[i-1][j-1][2]))
            dp[i][j][2] = max(dp[i][j][2] ,dp[i-1][j][2], max(dp[i-1][j-1][0] , dp[i-1][j-1][1]) )

        if Bessie[i-1] == "P":
            dp[i][j][0] = max(dp[i][j][0] ,dp[i-1][j][0] , max(dp[i-1][j-1][1] , dp[i-1][j-1][2]))

            dp[i][j][1] = max(dp[i][j][1] ,dp[i-1][j][1]  + 1  , max(dp[i-1][j-1][0] , dp[i-1][j-1][2])  + 1 )

            dp[i][j][2] = max(dp[i][j][2] ,dp[i-1][j][2]  , max(dp[i-1][j-1][0] , dp[i-1][j-1][1])  )
        
        if i == n :
            ans = max(dp[i][j][0] , dp[i][j][1] , dp[i][j][2])

with open('hps.out', 'w') as file:
    file.write(f"{ans}\n")