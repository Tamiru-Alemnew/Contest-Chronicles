n = int(input())
m = int(input())
flash = []
for _ in range(n):
    val = int(input())
    flash.append(val)
flash.sort(reverse=True)
cur = 0
for i in range(n):
    cur += flash[i]
    if cur >= m:
        print(i + 1)
        break