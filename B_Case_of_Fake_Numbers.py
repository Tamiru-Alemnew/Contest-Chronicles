n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if (a[i] - a[0] * (-1) ** i) % n != i:
        print("NO")
        exit()
print("YES")