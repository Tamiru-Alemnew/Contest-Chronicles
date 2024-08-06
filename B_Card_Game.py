import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

for i in range(ip()):
    a1, a2, b1, b2 = tip()
    suneet_wins = 0
    
    combinations = [
        ((a1, a2), (b1, b2)), 
        ((a1, a2), (b2, b1)),
        ((a2, a1), (b1, b2)), 
        ((a2, a1), (b2, b1))
    ]
    
    for s_cards, b_cards in combinations:
        suneet_round_wins = 0
        if s_cards[0] > b_cards[0]:
            suneet_round_wins += 1
        if s_cards[1] > b_cards[1]:
            suneet_round_wins += 1
            
        if suneet_round_wins > 1:
            suneet_wins += 1
            
    print(suneet_wins)

    