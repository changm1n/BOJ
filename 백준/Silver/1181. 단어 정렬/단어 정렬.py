N = int(input())
d = []
result= []
for i in range(N):
    a = str(input())
    d.append(a)
b = list(set(d))
result = sorted(b) 
result.sort(key=len) 
for i in result:
    print(i,end='\n')