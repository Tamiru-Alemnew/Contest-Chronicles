import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

n = ip()
graph = defaultdict(list)

for i in range(n-1):
    a , b = tip()
    graph[a].append(b)
    graph[b].append(a)


one = 0 
two = 0 

visited = [False]*(n+1)

stack =[(a , True)]

while stack :
    node , flag = stack.pop()

    if visited[node]:
        continue
    
    visited[node] = True
    one += flag 
    two += not flag

    for neighbor in graph[node]:
        stack.append((neighbor , not flag))


print(one*two - (n-1))