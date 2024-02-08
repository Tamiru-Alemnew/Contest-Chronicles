n = int(input())
for _ in range(n):
    x = int(input())
    arr = list(map(int, input().split()))
    sm = sum(abs(a) for a in arr)
    min_abs = min(abs(a) for a in arr)
    if 0 in arr or min_abs < 0:
        print(sm, 0)
    else:
        print(sm, 1)