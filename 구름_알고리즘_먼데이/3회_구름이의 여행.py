# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# def dfs(v, count=0):
# 	visited[v] = True
# 	if count > k:
# 		return -1
	
# 	for i in range(1,n+1):
# 		if graph[v][i] == 1 and not visited[i]:
# 			count += 1
			
# 			if i == n:
# 				visited[i] = True
# 				return 
# 			dfs(i, count)
from collections import deque

count = 0

def bfs(v):
	global count
	queue = deque([v])
	visited[v] = True
	
	while queue:
		v = queue.popleft()
		count += 1
		for i in range(1,n+1):
			if graph[v][i] == 1 and not visited[i]:
				queue.append(i)
				visited[i] = True
				if i == n:
					count += 1
					return count
				# print(count)

	
	
n, m, k = map(int, input().split())
graph = [[0]* (n+1) for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
	a, b = map(int, input().split())
	graph[a][b] = graph[b][a] = 1

bfs(1)

print(count)
if count <= k and visited[n]:
	print('YES')
else:
	print('NO')