x = int(input())

for i in range(x):
    a , b , c = map(int , input().split()) 
    print( ((a + c )// a ) + ((b + c) // b) )

