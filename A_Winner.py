import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right as br, bisect_left as bl; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()
 
x = ip()
cur = defaultdict(int)
mx = ["" , float("-inf")]
arr = []
for i in range(x):
    n , s = lcp()
    s = int(s)
    cur[n] += s 
    arr.append([n , cur[n]])

for n , key in cur.items():
    if key > mx[1] :
        mx =[n , key]
winner = set()
for n , key in cur.items():
    if key >= mx[1]:
        winner.add(n)

for n , key in arr:
    if n in winner and key >= mx[1]:
        print(n)
        break

