import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()

grid = []

for i in range(n):
    grid.append(lip())

def chk(r , c , sm):
    for i in range(n):
        for j in range(n):
            if grid[r][i] + grid[j][c] == sm:
                return True
            
    return False

flag = True
for r in range(n):
    for c in range(n):
        if grid[r][c] != 1:
            if not chk(r , c , grid[r][c]):
                flag = False

if flag :
    print("Yes")
else:
    print("No")