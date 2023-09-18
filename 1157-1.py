S = input()
s1 = S.upper()
a= []
c=[]
d=[]
d1 = []
e = 0
f= 0
g = 0
for i in range(len(S)):
    a.append(s1[i])
b = set(a)
c = list(b)
for i in range(len(c)):
    for j in range(len(s1)):
        if c[i] == s1[j]:
            d.append(s1.count(s1[j]))
            break
d1 = d.copy()
d1.sort(reverse=True)
e = d1[0]
for i in range(len(d)):
    if d[i] == e:
        f += 1
        g = i
if f != 1:
    print("?")
elif f == 1:
    print(c[g])

