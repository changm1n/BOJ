N = int(input())
s,m,l,xl,xxl,xxxl = map(int,input().split())
sizes = [s,m,l,xl,xxl,xxxl]
#size = list(map(int,input().split()))
t, p = map(int,input().split())
tshirt = 0
pen = 0
pen1 = 0
for i in range(6):
    if sizes[i] == 0:
        tshirt += 0
    elif sizes[i] // t == 0:
        tshirt += 1
    elif sizes[i] % t != 0:
        tshirt += sizes[i] // t + 1
    elif sizes[i] % t == 0:
        tshirt += sizes[i] // t
if N // p == 0:
    pen = 0
    pen1 = N % p
elif N // p != 0:
    pen = N // p
    pen1 = N % p
print(tshirt)
print(pen, pen1)