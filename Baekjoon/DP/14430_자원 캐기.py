import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (m+1)]
for i in range(n):
    temp = [0]
    for j in list(map(int, input().split())):
        temp.append(j)
    graph.append(temp)

for i in range(1, n+1):
    for j in range(1, m+1):
        graph[i][j] += max(graph[i-1][j], graph[i][j-1])
        
print(graph[n][m])