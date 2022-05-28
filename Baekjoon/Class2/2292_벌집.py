n = int(input())
# 1, 7, 19, 37, 61 (6, 12, 18, 24)
count = 1
cnt = 1
while count < n:
    count += 6 * cnt
    cnt += 1
print(cnt)