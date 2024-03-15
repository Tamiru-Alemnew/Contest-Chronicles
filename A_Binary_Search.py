y , m = map(int , input().split())

arr = list(map(int , input().split()))
q = list(map(int , input().split()))

for n in q :
    l , r = 0 , y - 1 
    while l <= r : 

        md = (l + r )//2 

        if arr[md] == n : 
            print("YES")
            break
        if arr[md] > n :
            r = md - 1
        else:
            l = md + 1
    else:
        print("NO")

