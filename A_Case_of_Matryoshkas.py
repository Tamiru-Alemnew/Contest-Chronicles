import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

t , k = tip()
ans = 0 
ar = lip()
l = [ar[-1] , ar[0]]

for i in range(k-1):
    arr = lip()
    n = arr[0]

    if arr[1] < l[0]:
        ans = n - 1 + l[0] - 1
        ans += n + l[0] - 1
    else:
        ans += 1

    l[0] = arr[-1]
    l[1] = n + l[0] 

    print(l)
    print(ans , n)
print(ans)




    










