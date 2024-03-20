import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
x = ip()
player = defaultdict(int)

for i in range(x):
    seg = lcp()
    seg[-1] = int(seg[-1])
    player[seg[0]] = max(player[seg[0]] , seg[-1])

pt = sorted(player.items(), key=lambda item: -item[1])

y = len(pt)
print(len(pt))

for i in range(len(pt)):
    if pt[i][1] < pt[i-1][1] :
        y = len(pt) -i

    l = y / len(player)
    if l < 0.5:
        print(pt[i][0] , "noob")
    elif l <0.8:
        print(pt[i][0],"random")

    elif l < 0.9:
        print(pt[i][0] , "average")

    elif l < 0.99:
        print(pt[i][0], "hardcore")
    else:
        print(pt[i][0] , "pro")

        

