m , n = map(int,input().split())

tzy = []
cur = [0]*n
for i in range(n):
    z , y , u = map(int,input().split())
    tzy.append([z , y , u])

def check(time):
    i = 0 
    c = 0 
    for t , z , y in tzy:
        tp = 0 
        tt = 0
        while tt + t <= time:
            tt += t + y
            tp += z
            c += z
        cur[i]=tp
        i += 1
    return c >= m
            
l , r = 0 , 100

while l + 1 < r :
    md = (l + r )//2

    if check(md):
        r = md 

    else:
        l = md 

print(r)
print(*cur)