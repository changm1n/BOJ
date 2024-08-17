def pal(N):
    s = str(N)
    for i in range(len(s)//2):
        if(s[i] != s[len(s)-1-i]):
            return False
    return True

N = int(input())
while N != 0:
    if(pal(N) == False):
        print("no")
    else:
        print("yes")
    N = int(input())