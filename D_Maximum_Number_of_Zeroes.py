import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0
from decimal import Decimal

n = ip()
count = defaultdict(int)
a = lip()
b = lip()
z,ans=0,0

for i in range(n):
    if a[i]==0:
        if b[i]==0:
            z+=1
    else:
        d=Decimal(-b[i])/Decimal(a[i])
        count[d] +=1
        ans=max(ans,count[d])
print(ans+z)

    