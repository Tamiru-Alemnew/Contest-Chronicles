import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    n , m = tip()
    grid = []
    ind = {}

    first = []
    for i in range(n):
        temp = lip()
        grid.append(temp)
        first.append(temp[0])
        ind[temp[0]] = temp

    col = []
    for j in range(m):
        cur = lip()
        if sorted(cur) == sorted(first):
            col = cur

    for r in col:
        row = ind[r]
        print(*row)




        
        

    



