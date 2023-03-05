n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

temp = []
def dfs():
    if len(temp) == m:
        print(*temp)
        return
    
    for i in arr:
        if i not in temp:
            temp.append(i)
            dfs()
            temp.pop()

dfs()