import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

class UnionFind:
    def __init__(self , n):
        self.parent = [i for i in range(n)]
        self.rank = [0 for _ in range(n)]
    def find(self , node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    def union(self , node1 , node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1


for i in range(ip()):
    N = ip()

    arr = lip()
    graph = defaultdict(set)

    for i , v in enumerate(arr):
        graph[i+1].add(v)
        graph[v].add(i+1)

    un = UnionFind(N+1)
    possible = set()

    for i in range(len(arr)):
        un.union(i+1 , arr[i])
        
    for i in range(len(arr)):
        possible.add(un.find(i+1))

    bamboo = 0 
    visited = set()

    for key , val in graph.items():
        if len(val) < 2 and un.find(key) not in visited:
            bamboo += 1
            visited.add(un.find(key))
    
    print(min(1 + len(possible) - bamboo ,  len(possible)), len(possible))


    
