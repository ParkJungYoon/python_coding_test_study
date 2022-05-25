n = int(input())
info = [list(map(int,input().split())) for i in range(n)]
result = []
for i in range(n):
    count = 1
    x, y = info[i]
    for j in range(n):
        xx, yy = info[j]
        if xx > x and yy > y:
            count += 1
    result.append(count)
print(*result)