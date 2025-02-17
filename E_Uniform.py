import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

word1 = cip()
word2 = cip()
ans = 0

graph = defaultdict(list)
edges = {}
for _ in range(ip()):
    a, b, w = input().split()
    if (a, b) in edges:
        edges[(a, b)] = min(int(w), edges[(a, b)])
    else:
        edges[(a, b)] = int(w)

for key, val in edges.items():
    a, b = key
    graph[a].append((b, val))

def shortest(s, e):
    heap = []
    heappush(heap, (0, s))
    distances = {s: 0}

    while heap:
        w, node = heappop(heap)
        
        for nbr, wt in graph[node]:
            new_dist = w + wt
            if nbr not in distances or new_dist < distances[nbr]:
                distances[nbr] = new_dist
                heappush(heap, (new_dist, nbr))
 
    return inf if e not in distances else distances[e]

answer = []

if len(word1) == len(word2):
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            cc = shortest(word1[i], word2[i])
            dd = shortest(word2[i], word1[i])
            if cc == dd == inf:
                print(-1)
                break
            elif cc < dd:
                answer.append(word2[i])
                ans += cc
            else:
                answer.append(word1[i])
                ans += dd
        else:
            answer.append(word1[i])
    else:
        print(ans)
        print("".join(answer))
else:
    print(-1)