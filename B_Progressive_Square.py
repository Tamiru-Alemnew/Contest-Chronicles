import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

# ai+1,j=ai,j+c
# ai,j+1=ai,j+d


for _ in range(ip()):
    n , c , d = tip()
    ar = lip()
    ar.sort()

    grid = [[0]*n for _ in range(n)]
    grid[0][0] =ar[0]
    
    for i in range(n):
        for j in range(1 ,n):
            grid[i][j] = grid[i][j-1] + d
        if i == n-1:
            break
        grid[i+1][0] = grid[i][0] + c

    arr=[]
    for j in range(n):
        arr.extend(grid[j])

    arr.sort()

    if ar == arr:
        print("YES")
    else:
        print("NO")
     


    


    