x = int(input())

for i in range(x):
    person , chair = map(int,input().split())
    space = list(map(int,input().split()))
    space.sort(reverse=True)
    t = 0
    for s in space:
        t += s
    if t > chair - person:
            print('NO')   
    else:
        t -=space[-1]
        t += space[0]
        if t > chair - person:
            print('NO')
        else:
            print('YES')