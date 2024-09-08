import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

grid = [[0]*n for i in range(n)]

for i in range(n):
    cur = lip()

    for j ,a in enumerate(cur):
        grid[i][j] = a


mine = grid[0][0]

for i in range(1,n):

    if mine >= i + 1:
        mine =  grid[mine-1][i]
    else:
        mine = grid[i][mine-1]

print(mine)
