import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

word1 = cip()
word2 = cip()

dp = [[0]*(len(word1)+1) for i in range(len(word2) + 1)]

for i in range(len(dp)):
    dp[i][0] = i 

for i in range(len(dp[0])):
    dp[0][i] = i


for i in range(1 ,len(word2)+1):
    for j in range(1 , len(word1)+1):
        if word1[j-1] == word2[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j] , dp[i][j-1] , dp[i-1][j-1])


print(dp[len(word2)][-1])