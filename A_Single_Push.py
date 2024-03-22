import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

t = ip()

for i in range(t):
    n = ip()
    a = lip()
    b = lip()

    count = defaultdict(list)

    for i in range(n):
        if a[i] != b[i]:
            count[b[i] - a[i]].append(i)
            cur = b[i] - a[i]

    if len(count) > 1 :
        print("NO")
    elif cur < 0:
        print("NO")
    else:
        tt = False
        if len(count) == 0:
            print("YES")
            tt = True
        if len(count[cur]) < 3:
            if len(count[cur]) ==1:
                print("YES")
                tt = True
            if len(count[cur]) == 2:
                l , q  = count[cur]
                if l +1 == q :
                    print("YES")
                    tt =True

            
        if len(count[cur]) == 3:
            l , q , r = count[cur]
            if l +1 == q :
                print("YES")
                tt =True
            else:
                print("NO" )
                tt =True

        if not tt:
            print("NO")


        



