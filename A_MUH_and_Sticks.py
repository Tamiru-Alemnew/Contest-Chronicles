import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip()


arr = lip()
count = Counter(arr)
leg = count.most_common()

if leg[0][1] >= 4:

    if leg[0][1] == 6:
        print("Elephant")

    elif leg[0][1] == 5:
        print("Bear")

    elif leg[1][1] == 2:
        print("Elephant")
    else:
        print("Bear")
else:
    print("Alien")