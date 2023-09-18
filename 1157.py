s = input()
s1 = s.upper()
a = []
a1 = []
d = 0
c = 0
for i in range(len(s)):
    b = s1.count(s1[i])
    a.append(b)
a1 = a.copy()
a.sort(reverse=True)
if len(s) == 1:
    print(s1)
else:
    for i in range(len(a1)-1):
        if a1[0] < a1 [i+1]:
            a1[0] = a1[i+1]      
            c = i + 1
        else: c += 1
        if s1[c] == s1[i+1]:
            d += 1
if d == a.count(a[0]):
    print(s1[0])
elif  len(a) != 1 and a[0] == a[1]:
    print("?")
elif len(a) != 1:
    print(s1[c])

    



