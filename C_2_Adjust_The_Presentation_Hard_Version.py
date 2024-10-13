import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n , m , q = tip()

    arr = lip()
    bb = lip()

    check = set()
    ch = []
    correct
    for i in range(q):
        a , c = tip()
        bb[a] = c


    for b in bb:
        if b not in check:
            check.add(b)
            ch.append(b)
           
        if len(ch) == n :
            break
    
    if ch == arr[:len(ch)]:
        print("YA")

    else:
        print("TIDAK")
