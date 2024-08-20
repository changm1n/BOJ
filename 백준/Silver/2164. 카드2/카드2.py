from collections import deque
N = int(input())
deque = deque()
for i in range(1,N+1):
    deque.appendleft(i)
while len(deque) != 1:
    deque.pop()
    a = deque.pop()
    deque.appendleft(a)
print(deque.pop())