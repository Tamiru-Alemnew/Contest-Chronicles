n = int(input())

for _ in range(n):
    i, e, u = map(int,input().split())

    t = i
    if e % 3 == 0:
        t += e // 3
        if u % 3 != 0 :
            t += 1
        t += u // 3
        print(t)
    elif 3 -  (e % 3) > u :
        print(-1)
        continue
    else:
        if (e + u) % 3 != 0 :
            t += 1
        t += (e + u ) //3
        print(t)