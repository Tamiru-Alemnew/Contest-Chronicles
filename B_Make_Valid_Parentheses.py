arr = list(input())
stack=[]
ans = 0 
for i in range(len(arr)): 
    if arr[i] == "(":
        stack.append(arr[i])
    else:
        if stack :
            ans += 2
            stack.pop()

print(ans)
        
