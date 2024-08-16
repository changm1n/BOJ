N, M = map(int,input().split())
cards = list(map(int,input().split()))
result = []
for i in range (len(cards)-2):
    for j in range(i+1, len(cards)):
        for k in range(j+1, len(cards)):
            csum = cards[i] + cards[j] + cards[k]
            if(csum <= M):
                result.append(csum)
result.sort(reverse=False)
print(result[len(result)-1])
