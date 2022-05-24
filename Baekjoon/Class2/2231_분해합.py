import sys
input = sys.stdin.readline
n = int(input())

# 자릿수 len(str(n)), 시간복잡도 : 	68ms
def subtotal(n):
    target = abs(n - len(str(n))*9)
    if n < 10:
        for i in range(1,n):
            sum = i
            for j in str(i):
                sum += int(j)
            if sum == n:
                return i
    else:
        for i in range(target,n):
            sum = i
            for j in str(i):
                sum += int(j)
            if sum == n:
                return i
print(subtotal(n)) if subtotal(n) else print(0)

# 시간복잡도 : 	2432ms

# import sys
# input = sys.stdin.readline
# n = int(input())

# def subtotal(n):
#     for i in range(1,n):
#         sum = i
#         for j in str(i):
#             sum += int(j)
#         if sum == n:
#             return i
# print(subtotal(n)) if subtotal(n) else print(0)