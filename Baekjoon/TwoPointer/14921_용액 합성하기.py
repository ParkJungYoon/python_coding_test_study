n = int(input())
a = list(map(int, input().split()))

start, end = 0, n-1
answer = a[start] + a[end]

while start < end:
    current = a[start] + a[end]

    if abs(current) < abs(answer):
        answer = current
    if current < 0:
        start += 1
    else:
        end -= 1

print(answer)