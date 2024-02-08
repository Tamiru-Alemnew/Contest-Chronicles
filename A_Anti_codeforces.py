x = int(input())
cd = "codeforces"
for i in range(x):
    c = input()
    ans = 0 
    for i in range(10):
        if c[i] != cd[i]:
            ans += 1
    print(ans)
