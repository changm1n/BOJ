#에라토스테네스의 체
N = int(input())
number = list(map(int,input().split()))
def eratos(a,n):
    a[1] = 0
    i = 2
    while i <= n/2:
        j = 2
        while i * j <= n:
            a[i * j] = 0
            j += 1
        i += 1
    return a

number.sort(reverse=False)
s = number[len(number)-1]
A = list(range(s+1))
B = eratos(A,s)
C = []
t = 0
for i in range(s+1):
    if B[i]: C.append(B[i])
for j in range(len(C)):
    for k in range(len(number)):
        if C[j] == number[k]:
            t += 1
print(t)