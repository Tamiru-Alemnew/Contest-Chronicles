import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m = tip()
graph = defaultdict(list)

def is_bipartite(graph , n):
    colors = [-1]*n

    for start in range(n):
        if colors[start] == -1:  
            queue = deque([start])
            colors[start] = 1

            while queue:
                node = queue.popleft()

                for neighbor in graph[node]:

                    if colors[neighbor] == -1:  
                        colors[neighbor] = 1 if colors[node] == 2 else 2
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[node]:  
                        return False, colors  

    return True, colors

for i in range(m):
    a , b = tip()
    graph[a].append(b)
    graph[b].append(a)

ok , ans = is_bipartite(graph , n+1)

if ok :
    print(*ans[1:])
else:
    print("IMPOSSIBLE")


    