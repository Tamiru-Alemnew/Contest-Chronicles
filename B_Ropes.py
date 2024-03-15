n , k = map(int , input().split())
q = []
for i in range(n):
    q.append(int(input()))

def check(x):
    ans = 0

    if x == 0 : return True
    for l in q:
        ans += l//x

    return ans >= k

l , r = 0 , max(q)
lp = 70
while lp : 
    md = (l + r ) / 2
    if check(md):
        l = md
    else:
        r = md 

    lp -=1
print(l)