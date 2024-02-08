x = int(input())

for _ in range(x):
    n = int(input())
    s = input()
    inv = False
    last = None

    for i in range(n // 2):
        if s[i] != s[-i - 1]:
            if inv and i - 1 != last:
                print('No')
                break
            inv = True
            last = i
    else:
        print("Yes")