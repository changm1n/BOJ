N = int(input())
a = 0
b = 0
c = 5 * a + 3*b
d=[]
for a in range(1000):
    for b in range (1,(N-5*a)//3):
        if c == N:
            d.append(a+b)
if len(d) > 0:
    print(d[0])
if len(d) == 0:
    print(-1)

    

    