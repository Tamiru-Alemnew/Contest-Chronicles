n = int(input())
 
arr = list(map(int,input().split()))
c =0

for i in range(1,n-1):
    if arr[i] == 0:
        if arr[i-1] == 1 and arr[i+1] ==1:
            arr[i+1] = 0
            c += 1
            
print(c)