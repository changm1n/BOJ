N = int(input())
list =[]
for _ in range(N):
    a,b = map(int,input().split())
    list.append(a)
    list.append(b)
result = []
s = 1
for i in range(0,N*2,2):
    for j in range(0,N*2,2):
        if list[i] < list[j] and list[i+1] < list[j+1]:
            s+=1
    result.append(s)
    s = 1
for i in range(len(result)):
    print(result[i],end=' ')