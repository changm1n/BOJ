N = int(input())
num = []
for i in range(N):
    a = int(input())
    num.append(a)
num.sort(reverse=False)
for i in num:
    print(i,end='\n')