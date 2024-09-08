import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0; sip = lambda: sys.stdin.readline().strip();

class Node:
    def __init__(self ,val, left=None, right=None) -> None:
        self.val = val 
        self.left = left
        self.right = None

ans = []

dummy = Node(None)
last = Node(None , dummy )
dummy.right = last 

mp = defaultdict(deque)

for _ in range(ip()):
    current = input().split()

    if current[0] == "insert":
        x , y = current[1] , current[2]
        new = Node(x)

        if mp[y]:
            ly = mp[y][0]
            
            temp = ly.right 
            new.left = ly
            new.right = temp
            ly.right = new 
            temp.left = new 

            mp[x].append(new)

        else:
            temp = last.left 
            temp.right = new 
            new.left = temp 
            new.right = last 
            last.left = new 

            mp[x].append(new)

    else:
        w = current[1]

        if mp[w]:
            cur = mp[w].popleft()

            prev = cur.left 
            next = cur.right 
            prev.right = next 
            next.left = prev


current = dummy.right 

while current.val :
    ans.append(current.val)
    current = current.right

print(*ans)

            






    