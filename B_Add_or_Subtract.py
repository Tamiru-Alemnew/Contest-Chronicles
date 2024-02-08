x = int(input())

for i in range(x):
    a , b , c = map(int, input().split())
    if a + b ==c :
        print("+")
    else:
        print("-")