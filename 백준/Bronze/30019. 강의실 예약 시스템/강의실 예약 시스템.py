import sys

n,m = map(int,sys.stdin.readline().rstrip().split())
time = [[0,0] for _ in range(n)]

for i in range(m):
    k,s,e = map(int, sys.stdin.readline().rstrip().split())
    if time[k-1][1] <= s:
        print("YES")
        time[k-1][0] = s
        time[k-1][1] = e
    else:
        print("NO")