import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


for i in range(ip()):
    arr = cip()

    l = 0
    r = len(arr) -1

    for j in range(len(arr)):
        if arr[j] == "0":
            r = min(r , j)
        elif arr[j] =="1":
            l = max(l , j )
    
    print(r - l + 1)