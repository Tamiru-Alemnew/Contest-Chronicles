from math import *
n = int(input())
ans = 1
s = sqrt(n)
count = 1
while  count < s :
    if n % count == 0 :
        ans *= count
        ans *= n // count
    
    count +=1

if n % s == 0:
    ans *= int(s)

print(ans , 1)

