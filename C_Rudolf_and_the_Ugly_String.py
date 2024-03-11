x = int(input())

for i in range(x):
    n = int(input())
    arr = list(input())
    ans = 0
    # count the number of substring with mapie

    mapie = 0 

    for i in range(n-4):
        if arr[i] == "m" and arr[i+1] == "a" and arr[i+2] == "p" and arr[i+3] == "i" and arr[i+4] == "e":
            mapie += 1

    for i in range(1 , n-1):
        if arr[i] == "i":
            if arr[i-1] == "p" and arr[i+1] == "e":
                ans += 1
        if arr[i] == "a":
            if arr[i-1] == "m" and arr[i+1] == "p":
                ans += 1

    print(ans - mapie)

