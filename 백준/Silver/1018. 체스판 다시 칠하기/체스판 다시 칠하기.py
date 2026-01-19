n,m = map(int,input().split())
board = []
count = 0
count1 = 0
result = []
for i in range(n):
    board.append(input())

for d in range(0,n-7):
    for k in range(0,m-7):
        for i in range(d,d+8):
            for j in range(k,k+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'B':
                        count += 1
                    if board[i][j] != 'W':
                        count1 += 1
                if (i+j)%2 != 0:
                    if board[i][j] != 'W':
                        count += 1
                    if board[i][j] != 'B':
                        count1 += 1
        result.append(count)
        result.append(count1)
        count = 0
        count1 = 0
result.sort()
print(result[0])

            
    
    
