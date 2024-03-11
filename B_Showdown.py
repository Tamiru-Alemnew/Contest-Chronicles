x = int(input())
for _ in range(x):
    s = input()
    c1 = c2 = h1 = h2 = 0
    b1 = b2 = 5
    a = 10
    for i in range(10):
        if i % 2 == 0:
            if s[i] == '?':
                h1 += 1
            elif s[i] == '1':
                c1 += 1
            b1 -= 1

            if c1 + h1 > b2 + c2 or c2 + h2 > c1 + b1:
                a = i + 1
                break
        else:
            if s[i] == '?':
                h2 += 1
            elif s[i] == '1':
                c2 += 1
            b2 -= 1

            if c1 + h1 > b2 + c2 or c2 + h2 > c1 + b1:
                a = i + 1
                break
    print(a)