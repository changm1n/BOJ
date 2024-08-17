a = str(input())
b = str(input())
c = str(input())
list = [a,b,c]
for i in range(3):
    if(list[i] != "Fizz" and list[i] != "Buzz" and list[i] != "FizzBuzz"):
        ans = int(list[i]) + 3-i
        if(ans % 3 == 0 and ans % 5 == 0):
            print("FizzBuzz")
            break
        elif(ans % 3 == 0 and ans % 5 != 0):
            print("Fizz")
            break
        elif(ans % 3 != 0 and ans % 5 == 0):
            print("Buzz")
            break
        else:
            print(ans)
            break
    
