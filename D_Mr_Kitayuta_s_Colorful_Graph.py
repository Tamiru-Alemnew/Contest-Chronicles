import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def dfs(node , e):
    if node in visited:
        return 0
    
    visited.add(node) 

    if node[0] == e:
        return 1
    
    cur = 0
    for neighbor in graph[node[0]]:
        if neighbor[1] == node[1]:
            
            cur += dfs(neighbor , e)

    return cur



n , k = tip()

graph = defaultdict(list)

for i in range(k):
    a , b , c = tip()
    graph[a].append(( b , c))
    graph[b].append((a , c))

t = ip()

query = []

for i in range(t):
    query.append((tip()))

for a , b in query:
    ans = 0
    for node in graph[a]:
        visited = set()
        if node[0] == b:
            ans += 1
        else:
            ans += dfs(node , b)

    print(ans)

