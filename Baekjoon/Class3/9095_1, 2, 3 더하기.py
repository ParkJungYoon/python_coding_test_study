t = int(input())

# d[1] = 1
# d[2] = 2
# d[3] = 4
# d[4] = 7
# d[5] = 14
# (5)(3,2)(2,3)(3+1+1)(1+3+1)(1+1+3)(2+2+1)(2+1+2)(1+2+2)(2+1+1+1)(1+2+1+1)(1+1+2+1)(1+1+1+2)(1+1+1+1+1)

def solution(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return solution(n-1) + solution(n-2) + solution(n-3)

for _ in range(t):
    print(solution(int(input())))

