x = int(input())

for i in range(x):
    n = int(input())
    w = input()
    temp = w[0]
    c = 1
    l  , r = 0 , 1 
    while r < len(w) and  l< len(w):
        if w[r] not in temp:
            temp += w[r]
            r += 1
            c += 1
            l += 1
        else:
            l = r
            while w[l:r+1] in temp and r < len(w):
                r += 1
            temp +=w[l:r]
            c += 1
            l = r - 1
    if c < n:
        print("YES")
    else:
        print("NO")

