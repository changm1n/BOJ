a= []
s=[]
c = set()
for _ in range(10):
    n = int(input())
    a.append(n)
for i in range(10):
    b = a[i]%42
    c.add(b)
for j in range(42):
    if j in c:
        s.append(j)
print(len(s))

