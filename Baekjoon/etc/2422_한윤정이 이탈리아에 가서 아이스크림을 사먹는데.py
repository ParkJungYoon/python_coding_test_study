from collections import defaultdict

n, m = map(int, input().split())
ueg = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    ueg[a].append(b)
    ueg[b].append(a)

def check_ueg(i, arr):
    for u in ueg[i]:
        if u in arr: return True
    return False

answer = 0
arr = []
def dfs(start):
    global answer

    if len(arr) == 3:
        answer += 1
        return

    for i in range(start,n+1):
        if i not in arr and not check_ueg(i, arr):
            arr.append(i)
            dfs(i+1)
            arr.pop()

dfs(1)
print(answer)

'''
# 방법 2 : 인덱스로 바로 접근하여 훨씬 빠름
ice = [[False for _ in range(n)] for _ in range(n)]
for i in range(m):
    i1, i2 = map(int, input().split())
    ice[i1 - 1][i2 - 1] = True
    ice[i2 - 1][i1 - 1] = True

result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if not ice[i][j] and not ice[i][k] and not ice[j][k]:
                result += 1

print(result)
'''