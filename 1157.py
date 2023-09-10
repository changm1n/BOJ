s = input()
s1 = s.upper()
c=0
b = 0
a = s1.count(s1[0])
if len(s) == 1:
    print(s1)
for i in range(len(s)-1):
    if s1[i] == s1[i+1]:
        i += 1
    elif a < s1.count(s1[i+1]):
        a = s1.count(s1[i+1])
        b = s1[i+1]
    else:
        b = s1[i]
for j in range(len(s)):
    if b == s1[j]:
        print(b)
        c += 1
        break
    elif a == s1.count(s1[j]) and len(s) != 1:
        print("?")
        c += 1
        break
if c == 0 and len(s) != 1:
    print(b)


