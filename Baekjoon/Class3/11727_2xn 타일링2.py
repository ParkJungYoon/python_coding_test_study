'''
d[1] = 1
d[2] = 3
d[3] = 5
d[4] = 11
'''

d = [0] * 1001
d[1], d[2] = 1, 3

n = int(input())
if n > 2:
    for i in range(3, n+1):
        d[i] = d[i-1] + 2 * d[i-2]

print(d[n] % 10007)