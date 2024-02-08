x = int(input())

for i in range(x):
    y = int(input())
    n = list(map(int , input().split()))
    n.sort()
    for i in range(1,y):
        if n[i] == n[i-1]:
            print("NO")
            break
    else:
        print("YES")

