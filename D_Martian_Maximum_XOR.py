import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

trie = lambda : defaultdict([None , None])
root = trie()

def insert(n):
    cur = root

    for i in range(k-1 , -1, -1):
        if n & 1<<i :
            if not cur[1]:
                cur[1] = trie()
            cur =cur[1]
        else:
            if not cur[0]:
                cur[0] = trie()

            cur = cur[0]

def find(n):
    cur = root

    for i in range(k-1 , -1, -1):
        if n & 1<<i :
            cur =cur[1]
        else:
            if not cur[0]:
                cur[0] = trie()

            cur = cur[0]


for _ in range(ip()):
    n , k = lip()

    arr = lip()

    for a in arr:
        insert(a)

    


    


    