n , m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
l , r = 0 , 0 
ans = []
while l < n and r < m :
    if a[l] < b[r] :
        ans.append(a[l])
        l += 1
    else :
        ans.append(b[r])
        r += 1
while l < n:
    ans.append(a[l])
    l += 1
while r < m :
    ans.append(b[r])
    r += 1
print(*ans)
