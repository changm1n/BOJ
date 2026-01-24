T = int(input())
coin_types = [25,10,5,1]
count = []
for i in range(T):
    n = int(input())
    for coin in coin_types:
        print((n // coin),end=" ")
        n = n%coin
    count = []

