n = int(input())
top = list(map(int, input().split()))
new_top = []
result = []

for i in range(1, n+1):
    while new_top:
        if new_top[-1][1] > top[i-1]:
            result.append(new_top[-1][0])
            break
        else:
            new_top.pop()

    if not new_top:
        result.append(0)

    new_top.append([i,top[i-1]])

print(*result)

'''
# 시간 초과

for i in range(1, n+1):
    new_top.append([i,top[i-1]])

temp_top = []
result = []

for _ in range(n-1):
    current = new_top.pop()
    flag = False

    while new_top:
        num = new_top.pop()
        if num[1] > current[1]:
            result.append(num[0])
            temp_top.append(num)
            flag = True
            break
        else:
            temp_top.append(num)

    if not flag:
        result.append(0)
    while temp_top:
        new_top.append(temp_top.pop()) 

result.append(0)
print(result[::-1])
'''
