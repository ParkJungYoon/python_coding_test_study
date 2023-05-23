'''
섬의 위치를 리스트로 가지고 있음.
그리고 그 섬을 하나씩 확인하면서 주변이 3이상 물이면 체크해뒀다가 마지막에 '.'로 처리
그리고 돌면서 'X' 50년 뒤에도 섬이 존재하는 위치의 최소 최대를 가지고 있다가 인덱싱해서 출력
'''

import sys
input = sys.stdin.readline

r, c = map(int, input().split())
graph = []
island = []
lost_island = []

dx, dy = (0, 1, 0, -1), (1, 0, -1, 0)

for i in range(r):
    temp = input()
    temp2 = []
    for j in range(c):
        if temp[j] == "X": island.append((i,j))
        temp2.append(temp[j])
    graph.append(temp2)

x_temp, y_temp = [], []

for check in island:
    water = 0
    for i in range(4):
        if 0 <= check[0] + dx[i] < r and 0 <= check[1] + dy[i] < c:
            if graph[check[0] + dx[i]][check[1] + dy[i]] == ".":
                water += 1
        else:
            water += 1
    if water >= 3:
        lost_island.append((check[0], check[1]))
    else:
        x_temp.append(check[0])
        y_temp.append(check[1])

for lost in lost_island:
    graph[lost[0]][lost[1]] = "."

result1 = graph[min(x_temp):max(x_temp)+1]
for result2 in result1:
    print(''.join(result2[min(y_temp):max(y_temp)+1]))