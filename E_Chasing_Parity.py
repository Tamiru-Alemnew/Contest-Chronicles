import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


n = ip()
a = lip()
graph = defaultdict(list)
dis = [-1]*n

for i in range(n):
    for m in [i+a[i], i-a[i]]:
        if -1 < m < n:
            if (a[m] & 1) == (a[i] & 1):
                graph[m].append(i)
            else:
                dis[i] = 1

q = deque([])
for i in range(n):
    if dis[i] != -1:
        q.append(i)

while q:
    # print(q)
    node = q.popleft()
    for nbr in graph[node]:
        if dis[nbr] == -1:
            dis[nbr] = dis[node]+1
            q.append(nbr)
    # print(dis)

print(*dis)
