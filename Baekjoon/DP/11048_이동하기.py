import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        max_num = 0
        if 0 <= i - 1 < n:
            max_num = max(max_num, room[i-1][j])
        if 0 <= j - 1 < m:
            max_num = max(max_num, room[i][j-1])
        if 0 <= i - 1 < n and 0 <= j - 1 < m:
            max_num = max(max_num, room[i-1][j-1])
        room[i][j] += max_num

print(room[n-1][m-1])