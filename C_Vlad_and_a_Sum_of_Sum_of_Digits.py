x = int(input())

sum_digits = [0] * (2*10**5 + 1)

for i in range(1, 2*10**5 + 1):
    sum_digits[i] = sum_digits[i-1] + sum(map(int, str(i)))

for _ in range(x):
    num = int(input())
    print(sum_digits[num])