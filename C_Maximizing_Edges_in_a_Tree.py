import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

graph = defaultdict(list)
t = ip()
for _ in range(t-1):
    v , e = tip()
    graph[v -1].append(e -1)
    graph[e -1].append(v -1)

color = [-1]*t
color[0] = 1
stk = [0]
vis = set([0])
r = 1
while stk:
    node = stk.pop()
    for nbr in graph[node]:
        if  color[nbr] == -1 :
            stk.append(nbr)
            color[nbr] = 1 - color[node]
            r += color[nbr] == 1
       

print(r*(t-r)-t+1)
