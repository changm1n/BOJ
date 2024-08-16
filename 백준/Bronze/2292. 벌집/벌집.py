N = int(input())
d = 0
n = 0
t = 2
for i in range(1,N+1):
    if(i == 1):
        d = 1
    if(i == t):
        d += 1
        n += 1
        t += 6*n
print(d)