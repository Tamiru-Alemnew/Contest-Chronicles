import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


sys.setrecursionlimit(2*10**5) 
n , m = lip()

graph = defaultdict(list)

for i in range(m):
    a , b = lip()
    graph[a].append(b)

def dfs(v):
    for u in graph[v]:
        if not dist[u - 1]:
            dist[u -1] = 1
            dfs(u)

flag = True
for i in range(1 , n+1):
    dist = [0]*n
    dist[i-1] = 1
    dfs(i)

    for j , d in enumerate(dist) :
        if d == 0:
            flag = False
            post = [i , j + 1]

    if not flag:
        break

if flag:
    print("YES")

else:
    print("NO")
    print(*post)



       