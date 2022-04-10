n, m = map(int,input().split())
j = int(input())
move = 0
now = [i for i in range(1,m+1)]
for _ in range(j):
    apple = int(input())
    if apple not in now:
        if apple < now[0]:
            distance = apple - now[0]
            move += abs(distance)
            now = list(map(lambda x:x+distance,now))
        else:
            distance = apple - now[-1]
            move += distance
            now = list(map(lambda x:x+distance,now))

print(move)