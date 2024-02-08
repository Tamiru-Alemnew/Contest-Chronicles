x = int(input())

for i in range(x):
    n = int(input())
    s = input()

    min_length = float('inf')
    count_a, count_b, count_c = 0, 0, 0

    for j in range(n):
        if s[j] == 'a':
            count_a += 1
        elif s[j] == 'b':
            count_b += 1
        elif s[j] == 'c':
            count_c += 1

        if count_a > count_b and count_a > count_c and j - i + 1 >= 2:
            min_length = min(min_length, j - i + 1)

    result = min_length if min_length != float('inf') else -1
    print(result)
