N = int(input())
for i in range(1,N+1):
    num = i+sum(map(int,str(i)))
    if N == num:
        print(i)
        break
    elif N == i:
        print(0)
        break
