T = int(input())
c = 0
while T > c:
    R, S = input().split()
    a = str(S)
    b = int(R)
    i = 0
    n = 0
    while len(a) > n:
        for _ in range(b):
            print(a[i:i+1],end='')
        i += 1
        n += 1
    c += 1
    print("")
