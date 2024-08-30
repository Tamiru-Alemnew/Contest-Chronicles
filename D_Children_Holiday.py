import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


n , m = tip()

query = []

for _ in range(m):
    query.append(lip())


tot = 0
def check (time ):
    global tot
    current = [0]*m
    total = 0 

    
    for i ,  (t , z , y) in enumerate(query):
         
         cur = (time // (t*z + y)) * z 
         cur += min(z, (time % (t*z + y)) // t)

         total += cur
         current[i] = cur

    tot = total
    return total >= n , current


l , r = 0 , 10**18 + 1

best = 0 
ans = []
while r - l >= 0 :
    md = (l + r)// 2 
    chk , dist = check(md)

    if chk:
        best = md 
        ans = dist[:]

        r = md - 1

    else:
        l = md + 1


print(best )
final = []

for a in ans:
    cur = min(a , n)
    final.append(cur)
    n -= cur 
    
print(*final)
