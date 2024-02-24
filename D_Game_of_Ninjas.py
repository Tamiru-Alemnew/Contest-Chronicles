arr = list(input())
stack = []
nar = 0 
sas = 0 
naruto = True
for s in arr:
    if stack and s == stack[-1]:
        stack.pop()
        if naruto:
            nar += 1 
            naruto = False
        else:
            sas += 1 
            naruto = True
        
    else:
        stack.append(s)

if nar > sas:
    print("YES")
else:
    print("NO")
