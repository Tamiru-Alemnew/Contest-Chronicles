x = int(input())

for i in range(x):
    b = input()
    if len(b)= 1:
        a = b
   
    else:
        a = b[:2] 
        for i in range(3 , len(b) , 2):
            a +=b[i]
    print(a) 