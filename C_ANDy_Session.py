for _ in range(int(input())):
    n , z = map(int , input().split())
    arr = [*map(int , input().split())]

    bit = [0]*30

    for num in arr:
        print(num.bit_length())
        binary = bin(num)

        for i , n in enumerate(reversed(binary)):
            if n == "b":
                break
            elif n == "1":
                bit[-(i+1)] +=1

    print(bit)

    for i in range(30):
        if z - bit[i] <= 0 : 
            z -= z - bit[i]
            bit[i] = len(arr)
            
            if z < 0 :
                break
    ans = []
    """
    10
    11
    """
    for b in bit:
        if b == len(arr):
            ans.append("1")

        else:
            ans.append("0")

    ans = "".join(ans)
    print(int(ans , 2))



            
