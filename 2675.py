T = int(input())
c = 0
while T > c:
    R, S = input().split()
    a = str(S)
    b = int(R)
    i = 0
    n = 0
    while len(a) > n:
        for _ in range(b):
            print(a[i:i+1],end='')
        i += 1
        n += 1
    c += 1
    print("")

# 문자열과 정수를 동시에 받는 것에서 헤맴
# 그냥 input split으로 받으면 str로 받아짐
# 받아서 타입 바꿔주면 해결