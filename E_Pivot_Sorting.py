from sys import stdin, stdout 

t  = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = sorted(a)
    pivot = -1
    for i in range(1, n):
        if a[i] < a[i-1]:
            pivot = i
            break
    if pivot == -1:
        x = 0
    else:
        x = (a[pivot-1] + a[pivot]) // 2
        a = [abs(ai - x) for ai in a]
        if sorted(a) != b:
            x = -1
    stdout.write(str(x) + "\n")