import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
from itertools import permutations

def f(a,x):
    if x//1e10>0:
        return
    a.append(x)
    f(a,x*10+4)
    f(a,x*10+7)

a,ans,i=[],0,0
f(a,4)
f(a,7)
a.sort()
L,R=tip()
while L<=R:
    while L>a[i]:
        i+=1

    ans+=a[i]*(min(a[i],R)-L+1)
    
    L=a[i]+1

print(ans)


    
