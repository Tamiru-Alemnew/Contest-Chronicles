x = int(input())
for i in range(x):
    str_input = input()
    pos = int(input()) - 1
    n = len(str_input)
    k = 0
    
    while pos >= n - k:
        pos -= (n - k)
        k += 1

    stack = []
    for i in range(n):
        while stack and stack[-1] > str_input[i] and k != 0:
            stack.pop()
            k -= 1
        stack.append(str_input[i])

    print(stack[pos], end="")
