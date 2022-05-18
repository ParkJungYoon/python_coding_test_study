i = 0
while 1:
    L, P, V = map(int,input().split())
    if L == 0 and P == 0 and V == 0:
        break
    vacation = L * (V // P)
    if V % P > L:
        vacation += L
    else:
        vacation += V % P
    i += 1
    print("Case " + str(i) + ": " + str(vacation))