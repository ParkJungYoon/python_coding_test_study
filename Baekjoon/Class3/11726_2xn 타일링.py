n = int(input())

# 비효율적 해법 : 재귀 -> 시간초과

def solution(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return solution(n-1) + solution(n-2)

print(solution(n) % 10007)

'''
n = 1 : 1
n = 2 : 2
n = 3 : 3
n = 4 : 5
'''

# 효율적인 해법: 다이나믹 프로그래밍
# 탑 다운 - 메모리제이션

d = [0] * 1001

def solution2(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    
    if d[n] != 0:
        return d[n]
    d[n] = solution2(n-1) + solution2(n-2)
    return d[n]

print(solution2(n) % 10007)