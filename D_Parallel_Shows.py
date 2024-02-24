n = int(input())
l = []
r = []

for _ in range(n):
    li, ri = map(int, input().split())
    l.append(li) 
    r.append(ri)

l.sort()
r.sort()

fa = fb = 0
for i in range(n):
    if fa < l[i]:
        fa = r[i]
    elif fb < l[i]:
        fb = r[i]
    else:
        print("NO")
        exit() 

print("YES")
