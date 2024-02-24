t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 30:
        print("NO")
    else:
        print("YES")
        num1, num2, num3 = 6, 10, 14
        rem = n - 30
        if rem == num1 or rem == num2 or rem == num3:
            num3 += 1
            rem -= 1
        print(num1, num2, num3, rem)