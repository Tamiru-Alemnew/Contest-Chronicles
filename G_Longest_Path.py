import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n , m = tip()

graph = defaultdict(list)
deg = [0 for i in range(n+1)]

for i in range(m):
    a , b = lip()
    graph[a].append(b)
    deg[b] += 1

queue = deque()
for i in range(1 , n +1):
    if deg[i] == 0 :
        queue.append(i)

l = 0   

while queue :
    for _ in range(len(queue)):
        node = queue.popleft()

        for nbr in graph[node]:
            deg[nbr] -= 1

            if deg[nbr] == 0:
                queue.append(nbr)

    l += 1


print(l-1)



