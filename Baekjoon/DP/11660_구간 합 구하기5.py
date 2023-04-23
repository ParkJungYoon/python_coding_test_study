import sys
input = sys.stdin.readline

n, m = map(int, input().split())

# 행 내에서 누적
graph = [[0]*(n+1)]
for i in range(n):
    temp = 0
    temp_list = [0]
    for j in list(map(int, input().split())):
        temp += j
        temp_list.append(temp)
    graph.append(temp_list)

# 열 단위로 누적
for i in range(1,n+1):
    for j in range(2,n+1):
        graph[j][i] += graph[j-1][i]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = graph[x2][y2]
    answer -= graph[x2][y1-1]
    answer -= graph[x1-1][y2]
    answer += graph[x1-1][y1-1]

    print(answer)

'''
# 행단위로만 누적했더니 시간 초과

graph = []
for i in range(n):
    temp = 0
    temp_list = [0]
    for j in list(map(int, input().split())):
        temp += j
        temp_list.append(temp)
    graph.append(temp_list)

print(graph)

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    row = graph[x1-1:x2]
    answer = 0
    for r in row:
        answer += r[y2] - r[y1-1]
    print(answer)
'''