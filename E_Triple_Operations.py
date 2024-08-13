import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def lgg (n):
    c = 0 
    while n :
        n //= 3
        c += 1
    return c

ps = [0]*(2*10**5 + 2)

for i in range(2*10**5+1):
    ps[i+1] = ps[i] + lgg(i)


for j in range(ip()):
    l , r = tip()

    ans = lgg(l)

    print(ps[r+1] - ps[l] + ans)

