n , s = map(int, input().split())
a = list(map(int, input().split()))
sm = 0 
l , r = 0 , 0 
ans = 0 
for r in range(n):
    sm +=a[r]
    while sm > s :
        sm -=a[l]
        l +=1
    ans =max(ans , r -l +1)
print(ans)