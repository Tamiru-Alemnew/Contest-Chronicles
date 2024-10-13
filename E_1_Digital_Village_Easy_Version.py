import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

import heapq

def dijkstra(graph, start):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start)) 
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  
    previous_vertices = {vertex: None for vertex in graph}  

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        
        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances, previous_vertices

for _ in range(ip()):
    n , m , p = lip()
    arr = lip()
    ans = defaultdict(int)

    un = UnionFind(n+1)



    for a in arr:
        result.append(ans[un.find(a)])


    print(*result)


