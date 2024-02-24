
x = int(input())
for i in range(x):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    marb = [0]*n
    for i in range(n):
        marb[i] =[a[i],b[i]]

    marb.sort(key = lambda x: x[0]+x[1])
    a_s = 0 
    b_s = 0 

    for i in range(n):
        if i % 2 == 0:
            a_s += marb[n-1-i][0] - 1
        else:
            b_s += marb[n-1-i][1] - 1

    print(a_s - b_s)
    
    

