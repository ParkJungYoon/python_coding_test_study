import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[int(i) for i in input().rstrip()] for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx, dy = (0,1,0,-1), (1,0,-1,0)

'''
3차원에 인덱스가 0이면 벽 부술 수 있는 횟수가 0인거고
1이면 횟수가 1번 남아있는거.
'''
def bfs(x,y):
    # 3번째 원소는 벽을 부술 수 있는 남은 횟수
    queue = deque([(x,y,1)])
    visited[x][y][1] = 1

    while queue:
        x, y, remain = queue.popleft()
        if x == (n-1) and y == (m-1):
            return visited[n-1][m-1][remain]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # 벽 안부수고 지나감, visited가 0이라는건 아직 방문전
                if graph[nx][ny] == 0 and visited[nx][ny][remain] == 0:
                    queue.append((nx,ny,remain))
                    # 그 자리에 벽을 안부순 경우(경로) 인덱스에 1을 더해줌. 0이 아닌 이상 이제 방문했다는 의미.
                    visited[nx][ny][remain] = visited[x][y][remain] + 1
                # 벽을 부술 횟수가 남아있어야함.
                elif graph[nx][ny] == 1 and visited[nx][ny][remain] == 0 and remain == 1:
                    queue.append((nx,ny,remain-1))
                    # 이제 벽을 한 번 부순 경로로 더해줌.
                    visited[nx][ny][remain-1] = visited[x][y][remain] + 1
    return -1

print(bfs(0,0))

'''
dp_map = [[sys.maxsize] * m for _ in range(n)]
dp_map[0][0] = 1

def bfs(x,y):
    queue = deque([(x,y,False)])

    while queue:
        print(dp_map)
        x, y, flag = queue.popleft()
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    queue.append((nx,ny,flag))
                    dp_map[nx][ny] = min(dp_map[nx][ny], dp_map[x][y]+1)
                    graph[nx][ny] = 2
                elif graph[nx][ny] == 1 and not flag:
                    queue.append((nx,ny,True))
                    dp_map[nx][ny] = min(dp_map[nx][ny], dp_map[x][y]+1)
                    graph[nx][ny] = 2
                
bfs(0,0)

if dp_map[n-1][m-1] == sys.maxsize:
    print(-1)
else:
    print(dp_map[n-1][m-1])
'''
    
'''
다른 노드에서 지나간 길을 못지나간다.
다른 노드에서 깼다고 판단하는 벽을 못건너감.

반례

2 4
0111
0010

ans: 5
'''