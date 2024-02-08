l , s = map(int,input().split())
q = list(input())

for i in range(s):
    j = 0
    while j < l-1:
        if q[j] == 'B' and q[j+1] == 'G':
            q[j] , q[j+1] = q[j+1] , q[j]
            j += 2
        else:
            j += 1
print(''.join(q))