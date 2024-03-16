n , x  , y = map(int , input().split())

def check(t):
    t -= min(x ,y)
    return ((t//x) +( t//y ) ) +1 >= n 

l , r = 0 , min(x , y )*n 

while l + 1 < r :
    md = (l + r ) //2

    if check(md):
        r = md
    else:
        l = md

print(r)
