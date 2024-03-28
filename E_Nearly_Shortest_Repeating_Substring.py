import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


for _ in range(ip()):
    n = ip()
    s = cip()

    for k in range(1, n):
        if n % k == 0:
            t = s[:k]
            t2 = s[-k:]
            mismatch = sum(s[i] != t[i % k] for i in range(n))
            mismatch2 = sum(s[i] != t2[i %  k] for i in range(n))
            if mismatch <= 1 or mismatch2 <= 1:
                print(k)
                break
    else:
        print(n)
