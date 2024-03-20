arr = list(map(int , input()))

o = 0 
z = 0 

for n in arr:
    if n == 1:
        o += 1 
        z = 0 
    else:
        z += 1 
        o = 0 

    if z >=7 or o >= 7:
        print("YES")
        break
else:
    print("NO")