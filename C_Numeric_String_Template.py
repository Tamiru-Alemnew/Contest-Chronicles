import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for j in range(ip()):
    a = ip()
    arr = lip()
    m = ip()
    mrr = []

    for i in range(m):
        mrr.append(cip())


    for mr in mrr:
        checker = {}
        mm = len(mr)

        if a != mm:
            print("NO")

        else:
            for i in range(a):
                if arr[i] in checker :
                    if checker[arr[i]] != mr[i]:
                        print("NO")
                        break

                elif mr[i] in checker:
                    if checker[mr[i]] != arr[i]:
                        print("NO")
                        break

                checker[arr[i]] = mr[i]
                checker[mr[i]] = arr[i]
            else:
                print("YES")

                