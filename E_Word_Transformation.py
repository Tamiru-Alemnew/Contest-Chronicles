import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for _ in range(ip()):
    word , need = input().split(" ")
    Count = Counter(need)
    found = set(need)
    occur = defaultdict(int)
    myWord = []
    for i in range(len(word)-1 , -1 , -1 ):
        if word[i] in found and occur[word[i]] < Count[word[i]]:
            myWord.append(word[i])
            occur[word[i]] += 1
        

    mine = "".join(myWord[::-1])

    if mine == need :
        print("YES")
    else:
        print("NO")


    



