t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    s = input()


    recolored = n
    black_count = 0
    left = 0
   
    for right, color in enumerate(s):
        black_count += (color == 'B')


        if right - left + 1 == k:
            recolored = min(recolored, k - black_count)
            black_count -= (s[left] == 'B')
            left += 1


    print(recolored)