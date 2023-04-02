# 풀이2 : 백트래킹 제대로 쓰기. 시간: 5420ms

import sys
input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
answer = sys.maxsize

def dfs(dep, idx):
    global answer
    if dep == n//2:
        start = 0
        link = 0
        for x in range(n):
            for y in range(n):
                if visited[x] and visited[y]:
                    start += s[x][y]
                elif not visited[x] and not visited[y]:
                    link += s[x][y]
        answer = min(answer, abs(start-link))
        return
    
    for i in range(idx,n):
        visited[i] = True
        dfs(dep+1, i+1)
        visited[i] = False

dfs(0,0)     
print(answer)

'''
풀이 1 : 시간 효율이 너무 안좋은 것 같음. 빡구현. 시간: 3144ms
import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

temp = []
result = []
def backtracking():
    if len(temp) == n//2:
        result.append([*temp])
        return

    for i in range(n):
        if i not in temp and (not temp or i > temp[-1]):
            temp.append(i)
            backtracking()
            temp.pop()

backtracking()

count = len(result) // 2
answer = sys.maxsize
for i in range(count):
    temp_start = result[i]
    temp_link = result[-(i+1)]
    start = 0
    link = 0
    for x,y in combinations(temp_start,2):
        start += (s[x][y] + s[y][x])
    for xx,yy in combinations(temp_link,2):
        link += (s[xx][yy] + s[yy][xx])

    answer = min(answer, abs(start-link))

print(answer)
'''


'''
0 1  - 여기
0 2  - 여기2
0 3  - 여기3
1 2  - 여기3
1 3  - 여기2
2 3  - 여기
'''