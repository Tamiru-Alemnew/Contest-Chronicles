from collections import defaultdict

x = int(input())

for i in range(x):
    n , k = map(int,input().split())
    a = list(map(int , input().split()))
    p = list(map(int , input().split()))
    mp = defaultdict(int)
    m = 1
    for i in range(n):
        mp[abs(p[i])] += a[i]
        m = max(m , abs(p[i]))


    mx = 0 

    for i in range(1, m+1):
        mx += k
        mx -= mp[i]

        if mx < 0:
            print("NO") 
            break
    else:
        print("YES")




    

