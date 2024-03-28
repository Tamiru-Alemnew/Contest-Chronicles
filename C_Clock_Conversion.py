import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math; 
ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0


def convert_to_12_hour_format(time_24):
    hour, minute = map(int, time_24.split(':'))
    if hour >= 12:
        if hour > 12:
            hour -= 12
        return f"{hour:02d}:{minute:02d} PM"
    else:
        if hour == 0:
            hour = 12
        return f"{hour:02d}:{minute:02d} AM"
    

for _ in range(ip()):
    time = input()

    print(convert_to_12_hour_format(time))