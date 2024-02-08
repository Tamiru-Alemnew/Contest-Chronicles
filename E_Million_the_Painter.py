from collections import Counter 
x = int(input())
w = list(input())
c = 1 if w[0] =="?" else 0
for i in range(1,x):
    if  w[i]=="?":
        c += 1     
    elif w[i]==w[i-1]:
        print("No")
        break      
else:
    if c > 1:
        print("Yes")
    else:
        if len(w) == 1 and c ==1:
            print("Yes")
        elif len(w) == 1 and c == 0:
            print("No")
        elif len(w) > 2 and c == 1:
            for i in range(1,len(w)):
                if w[i]=="?" and w[i+1] == w[i-1]:
                    print("Yes")
                    break
        else:
            c = Counter(w)
            y = c.get("Y",0)
            cy =c.get("C",0)
            m = c.get("M",0)

            if (y > 0 and cy==0 and m == 0) or (cy > 0 and y == 0 and m == 0) or (m>0 and cy == 0 and y == 0):
                print("Yes")
            else:
                print("No")





