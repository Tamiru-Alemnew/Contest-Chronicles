x = int(input())

for _ in range(x):
    n, t = map(int, input().split())
    
    seen = set()
    cur = []
    ans = 0 

    found = False
    for i in range(n+1):
        if i % 2 == 1:
            seen.add(i)
            cur.append(i)

        if t == i:
            ans = len(cur)  # Position of t in the odd numbers sequence
            found = True

    if not found:
        p = 1
        flag = False
        for i in range(2, 5):
            for num in cur:
                if i * num in seen:
                    flag = True
                    ans = len(cur) + p  # Position of t in the sequence
                    break
                else:
                    seen.add(i * num)
                    p += 1
            if flag:
                break

    print(ans)
