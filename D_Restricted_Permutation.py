import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , k = tip()

graph = defaultdict(list)
incoming = [0 for _ in range(n)]
for i in range(k):
    a , b = tip()
    graph[a].append(b)
    incoming[b-1] += 1

q = []
heapify(q)
ans = []
for i in range(n):
    if incoming[i] == 0:
        heappush(q ,i+1)

while q :
    node = heappop(q)
    ans.append(node)

    for nbr in graph[node]:
        incoming[nbr - 1] -= 1 

        if incoming[nbr - 1] == 0 :
            heappush(q , nbr)

if len(ans) == n:
    print(*ans)
    
else:
    print(-1)



