x = int(input())

for i in range(x):
    n , m = map(int, input().split())
    arr =list(map(int, input().split()))

    p=1 

    for i in arr:
        p*=i
    if 2023/p == 2023//p:
        print("YES")
        print(2023//p, "1 " *(m-1))
    else:
        print("NO")

    

    
    
