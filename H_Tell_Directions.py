import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m , k = tip()

grid = []

for i in range(n):
    grid.append(cip())

def inbound(row , col):
    return (0<= row < len(grid)) and (0<= col < len(grid[0]))

def dfs(row , col):
    if not inbound(row , col) or visited[row][col]:
        return
    visited[row][col] = True
    
    for dr , dc in directions:
        newRow , newCol = row + dr , col + dc
        dfs(newRow , newCol)


for r in range(n):
    for c in range(m):
        if grid[r][c] == "X":
            dfs(grid[r][c] )
