from collections import Counter
n = int(input())
for i in range(n):
    arr = list( input())

    count = Counter(arr)

    print(count.most_common(1)[0][0])
               