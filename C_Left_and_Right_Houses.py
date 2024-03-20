x = int(input())

for _ in range(x):
    n = int(input())
    arr = list(map(int, input()))

    ones = sum(arr)
    c1 = 0 
    ans = n + 5
    zeros = 0 
    
    if ones >= (n + 1)//2:
        ans = 0 

    for i in range(n):
        ones -= arr[i] == 1
        c1 +=arr[i] ==  1
        zeros += arr[i] == 0
        
        if zeros >= c1 and ones >= (n - i )//2:
            if abs(n/2 -(i+1)) < abs(n / 2 - ans):
                ans = i + 1 

    print(ans)
     