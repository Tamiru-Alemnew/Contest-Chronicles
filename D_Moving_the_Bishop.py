import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

n = ip()
si , sj = tip()
si -= 1
sj -= 1
ei , ej = tip()
ei -= 1
ej -= 1
grid = []

for _ in range(n):
    grid.append(cip())

directions = [ (1 , -1) , (-1 , 1) , (1 , 1) , (-1 , -1)]
def inbound(row , col):
    return (0<= row < n) and (0<= col < n)

q = deque([(si , sj , 5 , 0)])
visited = set([(si , sj ,0)])
ans = inf
flag = True
if grid[si][sj] == "#":
    flag = False

while q and flag:
    
    for _ in range(len(q)):
        r ,c ,pv , dp = q.popleft()
        if dp > n:
            continue
        if r == ei and c == ej and grid[r][c] !="#":
            ans = min(dp , ans)
            flag = False
            break
        
        for ind , dir in enumerate(directions):
            rc , cc = dir
            nr = r +  rc
            nc = c + cc
            temp = dp

            if inbound(nr , nc ) :
                if ind != pv:
                    temp += 1

                if (nr , nc ,temp) not in visited and grid[nr][nc]==".":
                    q.append((nr,nc , ind , temp))
                    visited.add((nr , nc ,temp))

if ans == inf:
    print(-1)
else:
    print(ans)
