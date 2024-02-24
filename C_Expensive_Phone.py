
sizes = int(input())
for _ in range(sizes):
    length = int(input())
    arr = list(map(int, input().split()))

    if length == 1:
        print(0)
        continue

    save = arr[-1]
    counts = 0

    for i in range(length - 2, -1, -1):
        if arr[i] > save:
            counts += 1
        else:
            save = arr[i]

    print(counts)

