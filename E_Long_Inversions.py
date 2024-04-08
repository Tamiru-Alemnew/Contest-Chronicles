import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


def check(mid, a, n):
    temp = a[:]
    for i in range(n):
        if temp[i] == 0:
            if i + mid > n: 
                return False
            for j in range(i, i + mid):  
                temp[j] = 1 - temp[j]
    return all(x == 1 for x in temp)

for _ in range(ip()):
    n = ip()
    a = cip()
    a = [int(i) for i in a]
    if sum(a) == 0 or sum(a) == n :
        print(n)
        continue

    l = 1
    r = n
    ans = 1
    for i in range(1 ,n+1):
        if check(i, a, n):
            ans = max(i , ans)
        
    print(ans)