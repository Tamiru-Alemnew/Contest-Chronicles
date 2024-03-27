import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

def HowMuch(x):
    res = 0
    while x % 2 == 0:
        res += 1
        x //= 2
    return res

for _ in range(ip()):
    n = ip()
    a = lip()
     
    s = 0 
    k = []
    for i in range(n):
        s += HowMuch(a[i])
        k.append(HowMuch(i+1))

    k.sort(reverse=True)
    i = 0
    while i < n and s < n:
        s += k[i]
        i += 1
    
    if s >= n:
        print(i)

    else:
        print(-1)

