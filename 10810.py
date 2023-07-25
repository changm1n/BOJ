N,M = map(int,input().split())
a = []
for _ in range(N):
    a.append(0)
for d in range(M):
    i,j,k = map(int,input().split())
    for b in range(i-1,j):
        a[b] = k
for c in range(N):
    print(a[c],end=' ')

