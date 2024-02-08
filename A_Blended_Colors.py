n = int(input())

for j in range(n):
    c = int(input())
    r1 = list(input())
    r2 = list(input())

    for i in range(c):
        if (r1[i] == "R" and r2[i] != "R") or (r2[i] =="R" and r1[i] != "R"):
            print("NO")
            break
    else:
        print("YES")