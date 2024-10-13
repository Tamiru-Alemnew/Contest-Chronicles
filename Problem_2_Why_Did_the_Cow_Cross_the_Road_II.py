import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def max_crosswalks(N, left_fields, right_fields):
    # Initialize the DP table
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Iterate over all pairs of fields
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            # Carry over previous values without making a new crosswalk
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            
            # If the fields are friendly, we can form a crosswalk
            if abs(left_fields[i-1] - right_fields[j-1]) <= 4:
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 1)
    
    return dp[N][N]

N = ip()

left_fields = [ip() for i in range(N)]
right_fields = [ip() for i in range(N)]

print(max_crosswalks(N, left_fields, right_fields))  
