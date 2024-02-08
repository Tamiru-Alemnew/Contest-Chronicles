l, r = map(int, input().split())

def different(x):
    digits = set(str(x))
    return len(digits) == len(str(x))

for x in range(l, r + 1):
    if different(x):
        print(x)
        break
else:
    print(-1)