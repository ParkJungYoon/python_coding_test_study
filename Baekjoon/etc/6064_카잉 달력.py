import sys
input = sys.stdin.readline

t = int(input())

'''
값을 동일하게 증가시키면서 결국 m, n 값을 얻기 위해서는
(k-x) % m == 0 : 즉, m의 배수이어야 한다.
(k-y) % n == 0 : 즉, n의 배수이어야 한다.
둘 중 하나의 조건만 만족하면 된다.

k = x or x + m or x + 2m ...
k에 m씩 더하면서 두 수의 곱보다 크면 답은 없다.
k = 3
3 + 10 * 1 = 13
3 + 10 * 2 = 23
'''

for _ in range(t):
    m, n, x, y = map(int, input().rstrip().split())

    k = x
    while True:
        if k > m * n:
            print(-1)
            break
        if (k-x) % m == 0 and (k-y) % n == 0:
            print(k)
            break
        k += m

'''
# 이렇게 값을 +1씩 더하면 시간초과가 날 수 밖에 없다.

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

    print(result)

'''
'''
반례
M % N == 0 일때 반례가 발생합니다.
'''