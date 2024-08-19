N = int(input())
result = []
for i in range(N):
    a,b = map(str,input().split())
    s=[int(a),b]
    result.append(s)
result.sort(reverse=False,key = lambda x:x[0])
for i in result:
    print(f"{i[0]} {i[1]}")