'''
d[1] = 1 **
d[2] = 1 **
d[3] = 1
d[4] = 2 **
d[5] = 2
d[6] = 3
d[7] = 4
d[8] = 5
d[9] = 7
d[10] = 9
'''

t = int(input())

d = [0] * 101
d[1], d[2] = 1, 1

for i in range(3, 101):
    d[i] = d[i-2] + d[i-3]

for _ in range(t):
    n = int(input())
    print(d[n])