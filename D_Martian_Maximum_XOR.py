import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;


for _ in range(ip()):
    n , k = lip()

    arr = lip()
    m = 2**k - 1
    arrs = sorted(arr)

    ans = [float("-inf") , -1 , -1]
    for i in range(1 , n ):
        cur = arrs[i] & arrs[i-1]
        temp = cur ^ m

        chk = (arr[i]^temp) & (arr[i-1]^temp)

        if chk > ans[0]:
            ans =[chk , arrs[i] , arrs[i-1]]

    print(ans )
    a = arr.index(ans[1])
    b = arr.index(ans[2])
    print( a + 1 , b + 1 , ans[0])


    