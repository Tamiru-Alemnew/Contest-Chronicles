x = int(input())

c={}
for i in range(x):
    n = input()  
    if n in c:
        c[n] += 1
        c[n+str(c[n])] = 0
        print(n+str(c[n]))
    else:
        c[n] = 0
        print("OK")