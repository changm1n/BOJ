g = []
for _ in range(28):
    a= int(input())
    g.append(a)
n = []
for i in range (1,31):
    n.append(i) 
for j in range (28):
    for k in range (1,31):
        if g[j] == k:
            n.remove(k)
print(n[0])
print(n[1])
            








    