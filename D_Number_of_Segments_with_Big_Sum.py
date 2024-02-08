n , m = map(int , input().split())
arr = list(map(int , input().split()))
sm = 0 
ans = 0 
l = 0 

for r in range(n):
    sm += arr[r]
    while sm >= m :
        ans += n -r
        sm -= arr[l]
        l += 1
print(ans)
    
