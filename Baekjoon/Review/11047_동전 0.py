n, k = map(int, input().split())
a = [int(input()) for i in range(n)]

result = 0

for i in range(n-1, -1, -1):
    if k // a[i] != 0:
        result += k // a[i]
        k %= a[i]
    if k == 0:
        break
print(result)