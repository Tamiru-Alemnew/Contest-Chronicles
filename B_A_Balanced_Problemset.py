import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

for _ in range(ip()):
    x , n = tip()

    div = set()
    for i in range(1, math.isqrt(x) + 1):
        if x % i == 0:
            if i * n <= x:
                div.add(i)
            if (x // i) * n <= x :
                div.add(x // i)

    print(max(div))