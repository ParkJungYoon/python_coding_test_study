# 백트래킹 (Backtracking)

현재 상태에서 가능한 모든 후보군을 따라 들어가며 탐색하는 알고리즘

## 예제

### 연습 문제 1 - N과 M (1)

```py
n, m = map(int, input().split())
arr = []
 
def dfs():
    if len(arr) == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        if i not in arr:
            arr.append(i)
            dfs()
            arr.pop()

dfs()
```

### 연습 문제 2 - N-Queen