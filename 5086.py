a,b = map(int,input().split())
while a and b != 0:
    if a and b == 0:
        break
    if a < b and b % a == 0:
        print("factor")
    elif a > b and a % b == 0:
        print("multiple")
    else: print("neither")
    a,b = map(int,input().split())