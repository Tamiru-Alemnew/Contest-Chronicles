from collections import Counter
x = int(input())
for i in range(x):
    n = int(input())
    word = []

    for j in range(n):
        word.extend(list(input()))

    count = Counter(word)

    for val in count.values():
        if val % n != 0 :
            print("NO")
            break
    else:
        print("YES")

        

    

    