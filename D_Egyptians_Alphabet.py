import sys; from collections import Counter, defaultdict, deque; from bisect import bisect_right , bisect_left ; from math import inf; from math import ceil ; import math;from heapq import *;ip = lambda: int(sys.stdin.readline().strip()); lip = lambda: list(map(int, sys.stdin.readline().strip().split())); tip = lambda: tuple(map(int, sys.stdin.readline().strip().split())); lcp = lambda: sys.stdin.readline().strip().split(); lsip = lambda: list(map(int, sys.stdin.readline().strip())); cip = lambda: list(sys.stdin.readline().strip()); sip = lambda: sys.stdin.readline().strip() ;even = lambda x: x & 1 == 0;

def add( a, b, p):
    return ((a % p) + (b % p)) % p

def subtract( a, b, p):
    return ((a % p) - (b % p)) % p

def multiply( a, b, p):
    return ((a % p) * (b % p)) % p

def binary_exponentiation( base, exponent, p):
    result = 1
    while exponent > 0:
        if exponent & 1:
            result =multiply(base, result, p)
        base = multiply(base, base, p)
        exponent >>= 1

    return result

def inverse( a, p):
    return binary_exponentiation(a, p - 2, p)

def division( a, b, p):
    return multiply(a, inverse(b, p), p)


n , m = tip()

arr1 = lip()
arr2 = lip()

mod = 10**9 + 7 
ans = 0 
for i in range(n-1 , -1 , -1):
    if arr1[i] != 0 and arr2[i] == 0 :
        if arr1[i] > arr2[i]:
            ans = 1
        elif arr1[i] < arr2[i]:
            ans = 0 
    elif arr1[i] == 0 and arr2[i] != 0 :
        rem = m - arr2[i]
        ans = division(ans , m , mod)
        ans += division(rem , m , mod)
    elif arr2[i] == 0 and arr1[i] != 0:
        rem = arr1[i] - m
        ans = division(ans , m , mod)
        ans += division(rem , m , mod)
    elif arr2[i]== arr1[i] == 0 :
        rem = m - 1
        ans = division(ans , m , mod)
        ans += division(rem , 2*m , mod)

print(ans)

    





