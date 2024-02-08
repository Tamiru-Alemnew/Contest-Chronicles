x = int(input())
s= []
for i in range(x):
    s.append(input())
s.sort(key= lambda x : len(x))

for i in range(x-1):
    if s[i] not in s[i+1]:
        print('NO')
        break
else:
    print('YES')
    for i in s:
        print(i)

