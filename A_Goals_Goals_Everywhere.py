import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n = ip()
    arr = lip()
    arr.sort()
    mx = sum(arr)
    lst = arr[-1]
    mn = 0 
    if n > 1:
        if lst > mx / 2:
            mn += lst - (mx // 2)
            
        mn += math.ceil(mx / 2) - mn
    else:z
        mn += arr[0]
    print(mn , mx)