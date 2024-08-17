def li(a,b):
    while a % b != 0:
        r = a % b
        a = b
        b = r
    if a % b == 0:
        return b
def ma(a,b):
    c = a
    d = b
    while(c != d):
        if(c < d):
            i = a
            while(c < d):
                c += i
        if(c > d):
            i = b
            while(c > d):
                d += i
    return c
    

a,b = map(int,input().split())
print(li(a,b))
print(ma(a,b))

