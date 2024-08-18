N = int(input())
num = []
for i in range(N):
    a = int(input())
    num.append(a)
result = list(set(num))
num.sort(reverse=False)
for i in num:
    print(i,end='\n')