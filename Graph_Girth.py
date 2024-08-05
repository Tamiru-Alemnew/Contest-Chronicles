import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

from collections import deque

maxn = 2510
inf = 1000000007

def cycle_len(start, n, adj):
    ans = inf

    dist = [-1] * n
    bfs = deque()

    dist[start] = 0
    bfs.append(start)

    while bfs:
        node = bfs.popleft()

        for adj_node in adj[node]:
            if dist[adj_node] == -1:
                dist[adj_node] = dist[node] + 1
                bfs.append(adj_node)
            elif dist[adj_node] >= dist[node]:
                ans = min(ans, 1 + dist[adj_node] + dist[node])

    return ans

def main():
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        adj[a].append(b)
        adj[b].append(a)

    res = inf
    for i in range(n):
        res = min(res, cycle_len(i, n, adj))

    if res == inf:
        print(-1)
    else:
        print(res)

if __name__ == "__main__":
    main()
