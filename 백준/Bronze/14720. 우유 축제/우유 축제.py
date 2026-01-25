n = int(input())
m = list(map(int, input().split()))
milk = [0,1,2]
count = 0
for i in range(len(m)):
    if m[i] == milk[0]:
        count += 1
        milk[0] = 3
    elif milk[0] != 0 and m[i] == milk[1]:
        count += 1
        milk[1] = 4
    elif milk[1] != 1 and m[i] == milk[2]:
        count += 1
        milk[0] = 0
        milk[1] = 1

print(count)