x = int(input())

for i in range(x):
    run = list(map(int,input().split()))

    c = 0 
    for i in range(1,len(run)):
        if run[i] > run[0]:
            c += 1
    print(c)

