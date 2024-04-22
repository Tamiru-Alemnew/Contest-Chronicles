import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n , k = tip()
    graph = defaultdict(list)
    incoming = defaultdict(int)
    undirected = []
    for i in range(k):
        d , a , b = tip()
        if d == 0:
            undirected.append((a , b))
        else:
            graph[a].append(b)
            incoming[b] += 1

    flag = True
    for a , b in undirected:
        if incoming[a] == 0 :
            graph[a].append(b)
            incoming[b] += 1
        elif incoming[b] == 0:
            graph[b].append(a)
            incoming[a] += 1
        else:
            flag = False

    if flag:
        print("YES")
        for key , values in graph.items():
            for val in values:
                print(key , val)

    else:
        print("NO")
