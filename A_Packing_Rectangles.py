w , h , n = map(int , input().split())

def check(x):
    if (x//w) * (x//h) >= n:
        return 1 
    else:
        return 0
    
l , r = 0 , max(w,h)*n

while l + 1 < r:
    md = (l + r) // 2 

    if check(md):
        r = md
    else:
        l = md
print(r)