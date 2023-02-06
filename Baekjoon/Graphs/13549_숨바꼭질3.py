from collections import deque
n, k = map(int, input().split())

# 내 현재 위치가 동생의 위치랑 같을 때까지
# 내가 선택할 수 있는 것은 -1 +1 중에서 빠른거 선택
queue = deque([n])
memo = [0] * 100001
visited = [False] * 100001

def bfs():
    while queue:
        current = queue.popleft()
        visited[current] = True
        if current == k: return memo[k]

        # 방문한 경우는 안들림. 3가지 경우를 들리는데 순간이동은 0초라서 순간이동부터 돌려줘야함.
        for next in (current*2, current-1, current+1):
            if 0 <= next <= 100000 and not visited[next]:
                if next != current*2: 
                    memo[next] = memo[current] + 1
                else:
                    memo[next] = memo[current]
                visited[next] = True
                queue.append(next)

print(bfs())