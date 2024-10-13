import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


n = ip()

arr = lip()

seg = []
answ = set()
curxor = 0 
for a in arr:
    answ.add(a)
    ind = bisect_right(seg , a)

    if ind == len(seg):
        seg.append(a)

    else:
        curxor ^= seg[ind]
        seg[ind] = a
    
    curxor ^= a 

    answ.add(curxor)

    
print(answ)