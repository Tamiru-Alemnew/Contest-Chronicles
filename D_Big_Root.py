import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    n = ip()
    v = lip()
    a = lip()
    
    graph = defaultdict(list)
    indegree = [0]*n

    for i in range(len(a)):
        graph[i+1].append(a[i]-1)
        indegree[a[i]-1] += 1

    
    queue = deque()
    
    for i , val in enumerate(indegree):
        if not val :
            queue.append(i)

        
    mn_vals = [float("inf")]*n


    while queue:
        node = queue.popleft()
        if node == 0 :
            break

        for nbr in graph[node]:
            indegree[nbr] -= 1
            mn_vals[nbr] = min(mn_vals[nbr] , v[node])

            if not indegree[nbr] :
                if nbr == 0:
                    break
                if mn_vals[nbr] < v[nbr]:
                    v[nbr] = mn_vals[nbr]
                else:
                    v[nbr] = (mn_vals[nbr] + v[nbr])//2


                queue.append(nbr)

    print(mn_vals[0] + v[0])






    

