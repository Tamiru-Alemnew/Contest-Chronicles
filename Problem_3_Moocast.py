import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

graph = [[0]*(25000+1) for i in range((25000+1))]
visited = [[0]*(25000+1) for i in range((25000+1))]

def inbound(row , col):
    return (0<= row < (25000+1)) and (0<= col < (25000+1))


for i in range(ip()):
    a , b , w = lip()

    graph[a][b] = w



