import math
t = int(input())

for i in range(t):
    h, w, n = list(map(int,input().split()))
    xx = math.ceil(n/h)
    yy = n%h
    if yy == 0 : yy = h
    if xx < 10: print(int(str(yy)+'0'+str(xx)))
    else: print(int(str(yy)+str(xx)))