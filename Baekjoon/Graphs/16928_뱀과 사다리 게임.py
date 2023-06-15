import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [0] * 101
visited = [False] * 101

ladder = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

snack = {}
for _ in range(m):
    u, v = map(int, input().split())
    snack[u] = v

def game_start(start):
    gamer = deque([start])
    visited[start] = True
    
    while gamer:
        current = gamer.popleft()
        
        for i in range(1,7):
            new = current + i
            if new in ladder.keys():
                new = ladder[new]
            elif new in snack.keys():
                new = snack[new]

            if new <= 100 and not visited[new]:
                dp[new] = dp[current] + 1
                gamer.append(new)
                visited[new] = True

game_start(1)
print(dp[100])

'''
# 메모리 초과
def game_start():
    gamer = deque([(1,0)])
    
    while gamer:
        current, count = gamer.popleft()
        if current == 100: break
        for i in range(1,7):
            new = current + i
            if new in ladder.keys():
                gamer.append((ladder[new], count + 1))
            elif new in snack.keys():
                gamer.append((snack[new], count + 1))
            else:
                gamer.append((new, count + 1))

    return count

print(game_start())
'''