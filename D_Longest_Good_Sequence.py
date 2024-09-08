n = int(input())
arr = list(map(int , input().split()))

dp =  [ [0]*(n+1) for i in range(n+1)]

for i in range(1 , n+1):
    for j in range(i+1):
        
