t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    ma = 0
    for ch in s:
        ma = max(ma, ord(ch))
    print(ma - 96)