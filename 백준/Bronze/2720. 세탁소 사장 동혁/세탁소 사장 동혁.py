T = int(input())
coin_types = [25,10,5,1]
count = []
a = []
for i in range(T):
    n = int(input())
    a.append(n)

for i in range(len(a)):
    for coin in coin_types:
        count.append(a[i] // coin)
        a[i] %= coin
    for j in range(4):
        print(count[j],end=" ")
    print("")
    count = []
