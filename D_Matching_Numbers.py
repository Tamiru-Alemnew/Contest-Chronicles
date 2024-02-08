x = int(input())

for i in range(x):
    n = int(input())

    if n % 2 == 0:
        print("No")
    else:
        print("Yes")
        for i in range(1,2*n,2):
            print(i,2*(n)-i)