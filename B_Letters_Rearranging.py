
x  = int(input())

for i in range(x):
    s = input().strip()
    if len(set(s)) == 1:
        print("-1")
    else:
        print(''.join(sorted(s)))




