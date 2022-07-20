# 단순 재귀 함수로 구현하면 지수 시간 복잡도라서 시간 초과
# 그래서 탑다운 메모이제이션 방식을 사용함.

# d 리스트로 한 번 계산된 결과를 메모이제이션 하기 위한 리스트 초기화
# 이미 계산한 적 있는 문제라면 그대로 반환
# 아직 계산하지 않은 문제라면 점화식에 따라서 결과 반환


from sys import stdin
input = stdin.readline

t = int(input())
d = [(0,0)] * 41
d[0] = (1,0)
d[1] = (0,1)

def fibo(n):
    if n <= 1: return d[n]
    for i in range(2,n+1):
        d[i] = (d[i-1][0]+d[i-2][0], d[i-1][1]+d[i-2][1])
    return d[n]

for _ in range(t):
    n = int(input())
    result = fibo(n)
    print(result[0], result[1])



## < 1차 시도 - 메모리 초과 >

# import sys
# input = sys.stdin.readline
# t = int(input())
# d = [0] * 41

# def fibo(n):
#     if n == 0: return 0
#     elif n == 1: return 1

#     if d[n] != 0:
#         return d[n]

#     d[n] = fibo(n-1) + fibo(n-2)
#     return d[n]

# for i in range(t):
#     n = int(input())
    
#     if n == 0: print(1,0)
#     elif n == 1: print(0,1)
#     else: print(fibo(n-1), fibo(n))


## < 2차 시도 - 시간 초과 >

# from sys import stdin
# input = stdin.readline

# t = int(input())
# d = [(0,0)] * 41
# d[0] = (1,0)
# d[1] = (0,1)

# def fibo(n):
#     if n <= 1: return d[n]
#     else:
#         fibo1 = fibo(n-1)
#         fibo2 = fibo(n-2)
#         # d[n] = tuple([sum(pair) for pair in zip(fibo1, fibo2)])
#         d[n] = (fibo1[0]+fibo2[0], fibo1[1]+fibo2[1])
#     return d[n]

# for _ in range(t):
#     n = int(input())
#     result = fibo(n)
#     print(result[0], result[1])