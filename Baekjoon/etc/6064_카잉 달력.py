import sys
input = sys.stdin.readline

t = int(input())

'''
값을 동일하게 증가시키면서 결국 m, n 값을 얻기 위해서는
(찾으려는 값-x) % m == 0 : 즉, m의 배수이어야 한다.
k % m = x % m
(찾으려는 값-y) % n == 0 : 즉, n의 배수이어야 한다.
'''

for _ in range(t):
    m, n, x, y = map(int, input().rstrip().split())
    if x == 1 and y == 1:
        print(1)
        continue

    x, y = x % m, y % n
    nx, ny = 1, 1
    result = 1

    while True:
        if nx == x and ny == y:
            break
        if nx == 0 and ny == 0:
            result = -1
            break
        nx = (nx + 1) % m
        ny = (ny + 1) % n
        result += 1
        print(nx,ny,result)

    print(result)


'''
반례
M % N == 0 일때 반례가 발생합니다.
'''