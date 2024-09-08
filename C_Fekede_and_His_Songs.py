import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m = lip()
music = []

for _ in range(n):
    c  , t = lip()
    music.append(c*t)

q = lip()

mp = {}

for i , qq in enumerate(q):
    mp[qq] = i


q.sort()


l = 0 
r = 0 
ans = [0]*m
cur = 0

while r < m and l < n :
    cur += music[l]

    while r < m and cur >= q[r]:
        ans[r] = l
        r+= 1

    l += 1

final = [0]*m

for i in range(m):
    final[mp[q[i]]] = ans[i] +1

for p in final:
    print(p)





