'''
1. end 올리다가 원하는 값 이상 되면 그때의 길이 저장
2. 여기서 start를 원하는 값 밑으로 떨어질 때까지 당김
3. 그리고 다시 오른쪽부터 올림
'''
n, s = map(int, input().split())
ss = list(map(int, input().split()))

sum = [0, ss[0]]
for i in range(1, n):
    sum.append(ss[i] + sum[i])

print(sum)

start, end = 1, 1
flag = False
result = 10 ** 9

while end <= n:
    check_sum = sum[end] - sum[start-1]
    if check_sum >= s:
        flag = True
        result = min(result, end - start + 1)
        start += 1
    else:
        end += 1

if flag:
    print(result)
else:
    print(0)

'''
반례
10 10
1 2 3 4 5 6 7 8 9 10
'''