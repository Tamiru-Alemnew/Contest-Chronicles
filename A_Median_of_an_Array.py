import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

x = ip()

for i in range(x):
    n = ip()
    arr = lip()
    arr.sort()

    c = 0
    if n % 2 == 0:
        j = n //2 -1
    else:
        j = n //2

    while j < n and arr[j] == arr[n//2] :
        c += 1
        j += 1
    print(1 if c == 0 else c)

