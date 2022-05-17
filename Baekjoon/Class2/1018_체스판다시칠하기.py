import sys
input = sys.stdin.readline
n, m = map(int,input().split())
map = [input() for _ in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7):
        cnt_w = 0
        cnt_b = 0
        for k in range(i,i+8):
            for kk in range(j,j+8):
                if ((k+kk)%2) == 0:
                    if map[k][kk] != 'W':
                        cnt_w += 1
                    else:
                        cnt_b += 1
                else:
                    if map[k][kk] != 'B':
                        cnt_w += 1
                    else:
                        cnt_b += 1
        result.append(min(cnt_w,cnt_b))
print(min(result))