import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

x = ip()

for i in range(x):
    n = ip()
    arr = lip()
    l = 0
    cur =[arr[0]]
    ans = ["1"]
    inc = True
    for j in range(1 ,n):
        tt = False
        if inc:
            if arr[j] >= cur[-1] :
                cur.append(arr[j])
                tt =True
            
            if arr[j] < cur[-1] and arr[j] <= cur[0]:
                inc = False
                cur.append(arr[j])
                tt = True

        else:
            if arr[j] >= cur[-1] and arr[j] <= cur[0]:
                cur.append(arr[j])
                tt = True

        if not tt:
            ans.append("0")
        else:
            ans.append("1")

    print("".join(ans))





    


