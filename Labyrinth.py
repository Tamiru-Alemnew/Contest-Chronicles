import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

h , w = tip()

grid = []
sr , sc = 0 , 0
for i in range(h):
    row = cip()
    if "A" in row:
        sr , sc = i , row.index("A")

    grid.append(row)


directions = [(1 , 0 ) , (0 , 1) , (-1 , 0) , (0 , -1) ]
dir = {}
dir[(1 , 0 )] = "D"
dir[(-1 , 0 )] = "U"
dir[(0, 1 )] = "R"
dir[( 0, -1 )] = "L"

def inbound(row , col):
    return (0<= row < len(grid)) and (0<= col < len(grid[0]))

def bfs(row , col ):
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    q = deque([(row , col , [""])])
    visited[row][col] = True

    while q:
        for _ in range(len(q)):
            row , col , path = q.popleft()
            if grid[row][col] == "B":
                return True , path
            
            for dr , dc in directions:
                newRow , newCol = row + dr , col + dc
                if inbound(newRow , newCol) and not visited[newRow][newCol] and grid[newRow][newCol] != "#":
                    cur = path[:]
                    cur.append(dir[((dr , dc))])
                    q.append((newRow , newCol , cur))
                    visited[newRow][newCol] = True
    return False , []

check , p = bfs(sr , sc )
   
if check :
    print("YES")
    ans = "".join(p)
    print(len(ans))
    print(ans)

else:
    print("NO")

            
