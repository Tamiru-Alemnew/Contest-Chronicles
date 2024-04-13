import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

n = ip()
graph = defaultdict(list)

for i in range(n-1):
    a , b , w = tip()
    graph[a].append((b , w))
    graph[b].append((a , w))

ans = 0
visited = set()
wh = 0 
def dfs(node , w):

    global wh , ans

    if node in visited:
        return
    visited.add(node)
    wh += w

    for nbr , wi in graph[node]:
        dfs(nbr , wi )
    
    ans = max(wh , ans)
    wh -= w

dfs(0 , 0)

print(ans)