import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
grid = []

for i in range(4):
    grid.append(cip())
found = False
for i in range(1,4):
    for j in range(1,4):
        c = 0 
        if grid[i][j] == "#":
            c += 1 
        if grid[i][j-1] == "#":
            c += 1 

        if grid[i-1][j] == "#":
            c += 1 
        if grid[i-1][j-1] == "#":
            c += 1

        if c >= 3:
            print("YES")
            found =True
            break
        if c <= 1:
            print("YES")
            found =True
            break

    if found:
        break
else:
    print("NO")



