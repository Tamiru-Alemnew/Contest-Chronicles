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


def main():
    with open('revegetate.in', 'r') as f:
        n, m = map(int, f.readline().strip().split())
        queries = [f.readline().strip().split() for _ in range(m)]
    
    un = UnionFind(n + 1)
    visited = set()
    ans = 1
    sm = UnionFind(n + 1)

    for query in queries:

        d, a, b = query
        a, b = int(a), int(b)

        un.union(a, b)

        if d == "S":
            sm.union(a, b)
        
    flag = True
    for d , a , b in queries:
        a, b = int(a), int(b)
        if d == "D":
            if sm.find(a) == sm.find(b):
                ans = 0 
                flag = False
    if flag:
        for i in range(1, n + 1):
            if un.find(i) not in visited:
                ans *= 2
                
            visited.add(un.find(i))

    with open('revegetate.out', 'w') as f:
        f.write(bin(ans)[2:] + '\n')

if __name__ == "__main__":
    main()




