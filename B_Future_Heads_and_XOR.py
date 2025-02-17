import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

a , c = tip()

bb = [0]*32
ans = 0
for i in range(32-1 , -1 , -1):
    ad = a // (3**i)
    a = a % (3**i)
    cd = c //(3**i)
    c = c% (3**i)

    ans += ((cd - ad) % 3)*(3**i)

print(ans)
