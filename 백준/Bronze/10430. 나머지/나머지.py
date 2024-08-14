A, B, C = map(int, input().split())
p = (A+B)%C
q = ((A%C)+(B%C))%C
r = (A*B)%C
s = ((A%C)*(B%C))%C
print(p)
print(q)
print(r)
print(s)