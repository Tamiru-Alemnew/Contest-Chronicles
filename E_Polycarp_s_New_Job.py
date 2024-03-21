import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

z = ip()

x , y = 0  , 0
for i in range(z):

    op , a , b = lcp()
    a = int(a)
    b = int(b)
    if op == "+":
        t = max(a , b )
        l  = min(a , b)
        y = max(t , y)
        x = max(l , x)
    else:
        t = max(a , b)
        l = min(a , b)

        if t >= y and  l >= x:
            print("YES")
        else:
            print("NO")



