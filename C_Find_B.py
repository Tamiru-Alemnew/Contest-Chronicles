x = int(input())

for i in range(x):
    n , k = map(int,input().split())
    arr = list(map(int,input().split()))
    ps = [0]*n
    ps[0] = 0 if arr[0] == 0 else 1
    for i in range(1 ,n):
        ps[i] += ps[i-1] 
        if arr[i] == 1:
            ps[i] +=  1
  
        
    for i in range(k):
        l , r = map(int,input().split())
        l -= 1
        r -= 1
        if ps[r] - ps[l] + 1 >= sum(arr[l:r+1]) -  ps[r] - ps[l] + 1 :
            print("NO")
        else:
            print("YES")

        

    

        
    