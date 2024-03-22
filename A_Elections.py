import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


n , c = tip()

cities = [0] *(n+ 1)

for i in range(c):
    arr =[0] + lip()
    b =  0

    for j in range(n+1):

        if arr[j] > arr[b] :
            b = j 

    cities[b] += 1 

mx =  0 

for v in range(n+1):
    if cities[v] > cities[mx] :
        mx = v

print(mx)



    

    
