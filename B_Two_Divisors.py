from math import gcd

def smallest_multiple(a, b):
    lcm = a * b // gcd(a, b)
    multiple = ((max(a, b) + lcm - 1) // lcm) * lcm
    while True:
        divisors = set()
        for i in range(1, int(multiple**0.5) + 1):
            if multiple % i == 0:
                divisors.add(i)
                divisors.add(multiple // i)
        if len(divisors) == 4:
            return multiple
        multiple += lcm

x = int(input())
for i in range(x):
    a, b = map(int, input().split())
    print(smallest_multiple(a, b))