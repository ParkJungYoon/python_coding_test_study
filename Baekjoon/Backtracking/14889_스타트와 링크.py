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
0 1  - 여기
0 2  - 여기2
0 3  - 여기3
1 2  - 여기3
1 3  - 여기2
2 3  - 여기
'''