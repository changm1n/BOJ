N,M = map(int, input().split())
l = list(range(1,N+1))
for k in range(1,M+1):
    i,j = map(int, input().split())
    if i == j:
        l[i-1] == l[j-1]
        break
    elif i - 1 == j-i:
        l[i - 1] == l[j-i]
        break
    else: 
        for t in range(1,(N//2+N%2)):
            l[i-1],l[j-1] = l[j-1],l[i-1]
            i += 1
    print(l)



print(l)
#k = 1
#while k < M+1:
    #i,j = map(int, input().split())
    
#for i in range(1,N//2+N%2):
    

