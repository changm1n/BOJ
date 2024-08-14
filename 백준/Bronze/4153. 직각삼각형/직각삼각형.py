i = 0
a,b,c = map(int,input().split())
while(i == 0):
    d = []
    d.append(a)
    d.append(b)
    d.append(c)
    d.sort(reverse=False)
    if d[0] > 0:
        if(d[0]*d[0] + d[1]*d[1] == d[2]*d[2]):
            print("right")
            a,b,c = map(int,input().split())
        else: 
            print("wrong")
            a,b,c = map(int,input().split())
    else: i += 1
