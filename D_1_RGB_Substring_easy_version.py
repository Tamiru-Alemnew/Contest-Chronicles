import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
x = ip()
t = "RGB"
for i in range(x):
    n , k = tip()
    arr = cip()
    ans = inf 
    for j in range(n - k + 1):
        for o in range(3):
            cur = 0 

            for p in range(k):
                if arr[j + p] != t[(p + o)%3]:
                    cur += 1
            ans = min(cur , ans )

    print(ans)
                






