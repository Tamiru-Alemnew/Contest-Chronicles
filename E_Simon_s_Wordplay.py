x = int(input())

for _ in range(x):
    n = int(input())
    words = [input() for _ in range(n)]
    mx = 0 
    for letter in 'abcde':
        def compr(word):
            w = letter
            return  (len(word)-word.count(w)) - word.count(w)
        words.sort(key = compr)
        l = 0 
        total = 0 
        cw = 0 
        for w in words:
            l += w.count(letter)
            total += len(w) - w.count(letter)

            if total < l:
                cw +=1 
                mx = max(cw, mx)
            else:
                break

    print(mx)

            
        

 