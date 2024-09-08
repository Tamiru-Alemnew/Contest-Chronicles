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
            self.rank[parent1] += self.rank[parent2]
        elif self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += 1

    def size(self , n):
        return self.rank[n]
    
n , m , k = lip()

home = lip()
hmm = set({*home})
un = UnionFind(n)
nodes = set()
for i in range(m):
    a , b = tip()
    if a not in hmm:
        nodes.add(a)
    if b not in hmm:
        nodes.add(b)

    un.union(a , b)


mx = 1

for h in home:
    size = un.size(un.find(h))
    mx = max(size , mx)



for n in nodes:
    mx *= un.size(un.find(n))

print(mx)