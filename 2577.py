a = int(input())
b = int(input())
c = int(input())
d = a*b*c
e = str(d)
f = 0
g = 0
for j in range(10):
    for i in range (len(e)):
        if int(e[i]) == g:
            f += 1
    print(f)
    f = 0
    g += 1        