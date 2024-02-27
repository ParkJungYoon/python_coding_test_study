import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[int(i) for i in input().rstrip()] for _ in range(n)]
b = [[int(i) for i in input().rstrip()] for _ in range(n)]

def change(x,y):
    global a
    for i in range(x, x+3):
        for j in range(y,y+3):
            if a[i][j] == 0:
                a[i][j] = 1
            else:
                a[i][j] = 0
    
count = 0
for i in range(0, n-2):
    for j in range(0,m-2):
        if a[i][j] != b[i][j]:
            change(i,j)
            count += 1

if a == b:
    print(count)
else:
    print(-1)
