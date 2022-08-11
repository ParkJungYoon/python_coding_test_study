def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(1,n+1):
        if i not in s:
            s.append(i)
            dfs()
            print(s)
            s.pop()

n, m = map(int, input().split())
s = []

dfs()

# 다른 풀이 (방문 여부를 리스트로 관리하는 경우)
# def dfs():
#     if len(s) == m:
#         print(' '.join(map(str, s)))
#         return
#     for i in range(1, n+1):
#         if visited[i]:
#             continue
#         visited[i] = True
#         s.append(i)
#         dfs()
#         s.pop()
#         print(s)
#         print(visited)
#         visited[i] = False
            

# n, m = map(int, input().split())
# s = []
# visited = [False] * (n+1)

# dfs()