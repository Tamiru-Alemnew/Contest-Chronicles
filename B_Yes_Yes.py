x = int(input())
for i in range(x):
    s = input()
    temp = "YesYes"
    temp += (len(s)//6 + 1) * temp
    if s in temp:
        print("YES")
    else:
        print("NO")
