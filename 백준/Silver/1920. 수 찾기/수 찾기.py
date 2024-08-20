import bisect
N = int(input())
A = list(map(int,input().split()))
M = int(input())
B = list(map(int,input().split()))
A.sort(reverse=False)
for i in range(M):
    if A[len(A)-1] < B[i]:
        print(0)
    elif A[bisect.bisect_left(A,B[i])] == B[i]:
        print(1)
    else:
        print(0)