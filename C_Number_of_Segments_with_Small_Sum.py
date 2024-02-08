n ,  m = map(int , input().split())
arr = list(map(int , input().split()))
l  = 0 
sm = 0
ans = 0 

for r in range(n):
    sm += arr[r]
    while sm > m:
        sm -=arr[l]
        l+=1 
    ans += r -l +1 
print(ans)

    