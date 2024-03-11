s = input()[::-1]
n = len(s) - 1
possibilities = {'1', '41', '441'}
current_str = ""
current_len = 0
result = 'YES'
for idx, i in enumerate(s):
    current_len += 1
    if current_len == 4:
        result = 'NO'
        break
 
    current_str += i
    if current_str in possibilities:
        current_str = ""
        current_len = 0
 
    elif n == idx:
        result = 'NO'
        break
 
print(result)