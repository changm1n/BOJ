l, p, v = map(int, input().split())
i = 0
while l != 0 and p != v and v != 0:
    result = int((v // p)*l)
    if (v % p) >= l:
         result += l
    else:
        result += (v %p)
    i += 1
    print("Case "+str(i)+":",result)
    l, p, v = map(int, input().split())
    