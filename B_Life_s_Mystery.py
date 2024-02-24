arr = list(input())
stack = []

for i in range(len(arr)):
    if stack and arr[i] == stack[-1]:
        stack.pop()
    else:
        stack.append(arr[i])
print("".join(stack))