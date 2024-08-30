import math

c = float(input())

l , r = 0 , 10**20

def check(x):
    return x**2 + math.sqrt(x)
    
while r - l > 0.0000001 :
    md = (l + r ) / 2 

    cur = check(md)
    if cur == c :
        print(md)
        break
    elif cur > c:
        r = md 

    else:
        l = md
else:
    print((l + r )/ 2)