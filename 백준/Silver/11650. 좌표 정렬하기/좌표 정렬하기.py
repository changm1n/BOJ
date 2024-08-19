N = int(input())
num = []
for i in range(N):
    a,b = map(int,input().split())
    s = [a,b]
    num.append(s)
num.sort(reverse=False)
for i in num:
    print(f"{i[0]} {i[1]}")