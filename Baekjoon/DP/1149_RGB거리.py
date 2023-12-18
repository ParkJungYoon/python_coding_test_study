import sys
input = sys.stdin.readline

n = int(input())
rgb_graph = [list(map(int, input().split())) for _ in range(n)]

'''
1번집 빨강 초록 노랑
     26  40  83
2번집 빨강 초록 노랑
     49  60  57
3번집 빨강 초록 노랑
     13  89  99
'''

'''
2번집부터 색을 고름. 빨강을 골랐을 때 1번집에서 초록 또는 노랑 중에 가장 작은 비용을 현재 고른 집 자리에 업데이트해줌.

step 1
1번집 빨강 초록 노랑
     26  40  83
2번집 빨강    초록    노랑
     49+40  60+26  57+26
3번집 빨강    초록    노랑
     13+83  89+83  99+86
'''

for i in range(1, n):
    # 빨강을 칠한 경우, 나의 앞 집에는 초록이나 노랑이 칠해진다.
    rgb_graph[i][0] = rgb_graph[i][0] + min(rgb_graph[i-1][1], rgb_graph[i-1][2])
    rgb_graph[i][1]
    # 초록을 칠한 경우, 나의 앞 집에는 빨강이나 노랑이 칠해진다.
    rgb_graph[i][1] = rgb_graph[i][1] + min(rgb_graph[i-1][0], rgb_graph[i-1][2])
    # 노랑을 칠한 경우, 나의 앞 집에는 빨강이나 초록이 칠해진다.
    rgb_graph[i][2] = rgb_graph[i][2] + min(rgb_graph[i-1][0], rgb_graph[i-1][1])

print(min(rgb_graph[n-1]))