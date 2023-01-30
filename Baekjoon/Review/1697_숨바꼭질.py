from collections import deque

n, k = map(int, input().split())
d = [0] * 100001

def bfs():
    queue = deque([n])

    while queue:
        cur = queue.popleft()
        if cur == k:
            return d[k]
        for next in (cur-1, cur+1, cur*2):
            if 0 <= next <= 100000 and d[next] == 0:
                d[next] = d[cur] + 1
                queue.append(next)

print(bfs())