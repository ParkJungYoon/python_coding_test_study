import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    closet = {}
    result = 1
    n = int(input())
    for i in range(n):
        name, type = input().strip().split()
        if type in closet.keys():
            closet[type].append(name)
        else:
            closet[type] = [name]

    keys = closet.keys()
    for key in keys:
        result *= (len(closet[key]) + 1)
    
    print(result - 1)
