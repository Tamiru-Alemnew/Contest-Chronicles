n = int(input())
vowels = set(["a" , "e" , "i" , "o" , "u" ,"y"])
arr = list(input())
ans =[]

for w in arr:
    if ans and ans[-1] in vowels and w in vowels:
        pass
    else:
        ans.append(w)

print("".join(ans))