s = input()
count_1 = []
count_2 = []
a = 0
b = 0

for i in range (len(s)):
    if s[i] == "0" and a == 0:
        count_1.append(i)
        a = 1
    elif s[i] == "1" and a == 1:
        count_1.append(i-1)
        a = 0
for i in range (len(s)):
    if s[i] == "1" and b == 0:
        count_2.append(i)
        b = 1
    elif s[i] == "0" and b == 1:
        count_2.append(i-1)
        b = 0

length_1 = len(count_1)
length_2 = len(count_2)

if length_1 % 2 != 0:
    count_1.append(0)
    length_1 += 1
if length_2 % 2 != 0:
    count_2.append(0)
    length_2 += 1
    
if length_1 > length_2:
    print(length_2 // 2)
elif length_2 > length_1:
    print(length_1 // 2)
elif length_1 == length_2:
    print(length_1 // 2)