import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
campus = []
doyeon = (0,0)
for i in range(n):
    temp = []
    temp1 = input().rstrip()
    for j in range(m):
        temp.append(temp1[j])
        if temp1[j] == "I":
            doyeon = (i,j)
    campus.append(temp)

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)
count = 0

def find_friend(x,y):
    global count
    queue = deque([(x,y)])

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if campus[nx][ny] == "P":
                    count += 1
                if campus[nx][ny] != "X" and campus[nx][ny] != "I":
                    queue.append((nx,ny))
                    campus[nx][ny] = "I"
    
find_friend(doyeon[0], doyeon[1])

if count == 0: print("TT")
else: print(count)
