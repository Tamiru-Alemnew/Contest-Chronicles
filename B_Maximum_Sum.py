import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

mod = 10**9 + 7
for _ in range(ip()):
    n , k = tip()

    arr = lip()
    s = sum(arr)
    mx = 0 
    cur = 0 
    for i in range(n):
        cur = max(arr[i], cur + arr[i])
        mx = max(mx, cur)

    x = mx

    if k == 1:
        print((s + x)%mod)
    else:
        print((s + (2 ** k) * x - x)%mod)


