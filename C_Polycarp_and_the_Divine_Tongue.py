t = int(input())
for _ in range(t):
    s = input()

    left = 0
    underline = 0

    for right in range(len(s)):
        if s[right] == 'w':
            if s[left] == 'w':
                underline += 1
                
            else:
                underline += 1 + (right - left)//2

            left = right + 1
        
    if left < len(s):
        underline += (len(s) - left)//2
    
    print(underline)