n = int(input())
seat = input()
cup = 1

cup += len(seat)
couple = seat.count('L')
cup -= int(couple//2)
if cup > len(seat):
    print(len(seat))
else:
    print(cup)