n, k = map(int, input().split())
a = list(map(int , input().split()))

def check(p):
    m = sum(ai - p for ai in a if ai > p)
    l = sum(p - ai for ai in a if ai < p)
    return m * (100 - k) / 100 >= l

l, r = 0.0, 1000.0
lp = 100
while lp:
    mid = (l + r) / 2
    if check(mid):
        ans = mid
        l = mid
    else:
        r = mid
    lp -= 1
print(ans)