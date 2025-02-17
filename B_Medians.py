import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n , k = tip()
    if (k == 1 and n != 1) or ( k == n and n != 1) :
        print(-1)
        continue
    if n==k ==1:
        print(1)
        print(1)
    elif even(k):
        print(3)
        print(*[1 , k , k+1])

    else:
        print(3)
        print(*[1 , k -1 , k + 2])