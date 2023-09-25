a, b, c, d, e, f, g, h = map(int,input().split())
arr = [a,b,c,d,e,f,g,h]

for i in range(0,8):
    if arr[i] + arr[7-i] == 9:
        if arr[0] == 1 and arr[1] == 2:
            if arr[2] == 3 and arr[3] == 4:
                print("ascending")
                break
            else : 
                print("mixed")
                break
        elif arr[0] == 8 and arr[1] == 7:
            if arr[2] == 6 and arr[3] == 5:
                print("descending")
                break
            else: 
                print("mixed")
                break
        else:
            print("mixed")
            break
    else: 
        print("mixed")
        break