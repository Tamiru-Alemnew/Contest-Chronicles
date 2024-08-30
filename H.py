import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
mp = [[] for i in range(26)]

arr = lip()
for i in range(26):
    cur = []
    for a in arr:
        heappush(cur , (-abs(i - a) , a ))

    mp[i] = cur

removed =set()

for i in range(n-1):
    ch = cip()

    ch = ord(ch[-1].lower()) - ord("a")

    while mp[ch][0][1] in removed :
        heappop(mp[ch])

    a , b = heappop( mp[ch])

    removed.add(b)

for a in arr :
    if a not in removed  :
        print(a)







