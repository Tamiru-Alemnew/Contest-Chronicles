import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

s = cip()
k = cip()

x = []
tobe = []
for i in range(len(s)):
    if s[i]!= k[i]:
        if ord(s[i]) > ord(k[i]):
            s[i] = k[i]
            x.append("".join(s))
        else:
            tobe.append(i)

for j in range(len(tobe)-1 , -1 , -1):
        i = tobe[j]
        s[i] = k[i]
        x.append("".join(s))

n = len(x)
print(n)

for i in range(n):
    print(x[i])