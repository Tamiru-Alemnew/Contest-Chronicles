import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    n , m = tip()

    arr = []

    for i in range(n):
        arr.append(list(map(int , input().split())))
    
    if len(arr[0]) == 1 and len(arr) == 1:
        print(-1)
        continue

    elif len(arr[0]) == 1:
        temp =  arr[len(arr)-1][0]

        for i in range(len(arr) - 2 , -1 , -1):
            arr[i+1][0] = arr[i][0]

        arr[0][0] = temp

    else:
        for j in range(len(arr)):
            temp = arr[j][len(arr[0])-1]
            for i in range(len(arr[0]) - 2 , -1 , -1):
                arr[j][i+1] = arr[j][i]

            arr[j][0] = temp

    for i in range(len(arr)):
        print(*arr[i])