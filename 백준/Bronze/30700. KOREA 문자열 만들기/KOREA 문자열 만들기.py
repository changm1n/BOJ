s = input()
count = 0
result = "KOREA"
idx_s = 0
if s.count("K") == 0:
    count = 0
else:
    for i in range(len(s)):
        if s[i] == result[idx_s]:
            count += 1
            if idx_s < 4:
                idx_s += 1
            else:
                idx_s = 0
print(count)