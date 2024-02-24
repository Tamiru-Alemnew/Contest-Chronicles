x = int(input())

for _ in range(x):
    n , k1 , k2 = map(int, input().split())
    w1 = list(map(int, input().split()))
    w2 = list(map(int, input().split()))

    if n in w1 :
        print("YES")
    else:
        print("NO")

