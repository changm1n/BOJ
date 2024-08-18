N = int(input())
list = []
result= []
for i in range(N):
    a = str(input())
    if(list.count(a) == 0):
        list.append(a)
result = sorted(list) 
result.sort(key=len) 
for i in range(len(result)):
    print(result[i])