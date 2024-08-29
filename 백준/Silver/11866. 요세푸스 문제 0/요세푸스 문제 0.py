from collections import deque
N, K = map(int,input().split())
a = []
for i in range (N):
    a.append(i+1)
num = deque(a)
result = []
while len(num) != 0:
    for _ in range(K - 1):
        num.append(num.popleft())
    result.append(num.popleft())
output = "<" +", ".join(map(str,result))+">"
print(output)