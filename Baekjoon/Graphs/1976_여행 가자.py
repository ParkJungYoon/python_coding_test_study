import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(int, input().split()))

# 1. 일단 각각의 집합으로 초기화하고
parents = [i for i in range(n+1)]

# 찾기(Find) 함수를 재귀적으로 호출한 뒤에 부모 테이블 값을 바로 갱신한다.
def find_parents(x):
    if parents[x] != x:
        parents[x] = find_parents(parents[x])
    return parents[x]

def union_find(a, b):
    a = find_parents(a)
    b = find_parents(b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b 

# 2. 연결되어 있는 도시끼리 합집합 시켜줌
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            print(i+1, j+1)
            union_find(i+1, j+1)

print(parents)
# 3. 여행 계획에 들어있는 도시가 모두 같은 집합인지 확인 or 사이클 판별 알고리즘
check = parents[plan[0]]
flag = True
for i in range(1, m):
    if parents[plan[i]] != check:
        flag = False

if flag: print("YES")
else: print("NO")


'''
반례: 여행계획이 1일 때 에러남

반례2
// input
5
5
0 1 1 0 0
1 0 0 0 0
1 0 0 0 1
0 0 0 0 1
0 0 1 1 0
1 2 3 4 5

// ans
YES

// wrong output
NO
'''