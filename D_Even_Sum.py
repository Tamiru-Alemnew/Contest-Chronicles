x = int(input())
n = list(map(int, input().split()))
o = []
e = 0
for i in range(x):
    if n[i]%2 == 0:
        e +=n[i]
    else:
        o.append(n[i])
if len(o)% 2==0:
    print(e+sum(o))
else:
    o.sort()
    print(e+sum(o)-o[0])



