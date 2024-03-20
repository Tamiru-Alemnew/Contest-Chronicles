import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
x = ip()

for i in range(x):
    n = ip()
    arr = cip()
    x , y = (0 , 0 )
    ind = {(x , y) : 0}
    ans = [float("-inf") , float("inf")]

    for r , l in enumerate(arr):
        if l == "L":
            x , y  = x - 1,y
        elif l == "R":
            x , y = x+1,y
        elif l == "U":
            x , y = x,y+1
        else:
            x , y = x, y - 1
        
        if (x , y) in ind:
            if (r - ind[(x , y)] ) < ans[1] - ans[0]:
                ans = [ind[(x , y)] + 1 , r + 1]
                
        ind[(x , y)] = r + 1

    if ans[0] != float("-inf"):
        print(*ans)
    else:
        print(-1)




        

