import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0

n = ip()
arr = lip()
color = lip()

graph = {i: [] for i in range(n)}
for i in range(n - 1):
    s = arr[i] - 1
    graph[s].append(i + 1)
 
ans = 1
stack = [0]
while stack:
    curr = stack.pop()
    for nbr in graph[curr]:
        clr = 1 if color[curr] != color[nbr] else 0
        ans += clr
        stack.append(nbr)
        
print(ans) 
    
