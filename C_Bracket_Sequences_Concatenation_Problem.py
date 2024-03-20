import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()

arr = []

def valid(s ):
    stack = []
    op = 0
    for i in range(len(s)):
        if s[i] == "(":
            stack.append(s[i])
        else:
            if not stack:
                op += 1
            else:
                stack.pop() 
    return len(stack) , op

x = ip()
valids = 0 
ans = 0 
op = defaultdict(int)
cl = defaultdict(int)

for i in range(x):
    temp = cip()
    arr.append(temp)

for temp in arr:
    opp , cll   = valid(temp)
    if cll == 0 and opp == 0:
        valids += 1 
    else:
        if opp > 0 and cll == 0:
            ans += cl[opp]
            op[opp] += 1
        elif cll > 0 and opp == 0:
            ans += op[cll]
            cl[cll] += 1 

ans += valids * valids

print(ans)