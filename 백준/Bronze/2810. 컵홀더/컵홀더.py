n = int(input())
seat = input()
cup = 1

cup += n
couple = seat.count('L')
cup -= int(couple//2)
if cup > n:
    print(n)
else:
    print(cup)