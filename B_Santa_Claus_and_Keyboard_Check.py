import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

fav = cip()
cur = cip()
check = {}

def solv(fav):
    ans = set()
    for i , f in enumerate(fav):
        if f in check or cur[i] in check:
            if f in check:
                if check[f] != cur[i]:
                    return -1  
            if cur[i] in check:
                if check[cur[i]] != f:
                    return -1              
        else:
            check[f] = cur[i]
            check[cur[i]] = f
            ans.add((check[f] , f))

    return ans

ans = solv(fav)
tmp = set()
if ans == -1:
    print(-1)
else:
    for k , val in ans :
        if k != val:
            tmp.add((k , val))

    print(len(tmp))
    for k , val in tmp:
        print(k , val )