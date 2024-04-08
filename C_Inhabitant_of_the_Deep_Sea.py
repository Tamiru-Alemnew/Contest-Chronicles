import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n , k = tip()

    s = lip()

    if sum(s) <= k:
        print(n)
        continue

    prefix = [0]*(n+1)

    for i in range(1, n+1):
        prefix[i] = prefix[i-1] + s[i-1]

    suffix = [0]*(n+1)
    for i in range(n-1, -1, -1):
        suffix[i] = suffix[i+1] + s[i]
    suffix.reverse()
    ans = 0

    if even(k):
        tt = k //2
    else:
        tt = k //2 + 1

    l = bisect_right(prefix, tt)
    r = bisect_right(suffix, k-tt)
    
    l -=1
    r -= 1

    ans = l + r

    print(ans)


            

