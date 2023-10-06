from collections import deque

n = int(input())
balloon = list(map(int, input().split()))

queue = deque([])
for i in range(1, n+1):
    queue.append((i, balloon[i-1]))

result = []

while queue:
    idx, number = queue.popleft()
    result.append(idx)

    if not queue:
        break

    if number > 0:
        for _ in range(number-1):
            queue.append(queue.popleft())
    else:
        for _ in range(abs(number)):
            queue.appendleft(queue.pop())

print(*result)