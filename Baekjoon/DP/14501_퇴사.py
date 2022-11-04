'''
시도1: 바텀업
테스트 케이스 4 실패 원인: 6일차에서 갈 수 있는건 무조건 7일차라고 생각함.
상담 시간 더 이후에 날짜로도 이동가능
'''

# n = int(input())
# table = [(0,0)]

# d = [0] * 16

# for i in range(n):
#     t, p = map(int, input().split())
#     table.append((t,p))

# print(table)

# for i in range(1, n+1):
#     if i + table[i][0] <= n+1:
#         d[i] = table[i][1]
#         next = i
#     else:
#         continue
#     while True:
#         next =  next + table[next][0]

#         if next > n or next + table[next][0] > n+1:
#             break

#         d[i] += table[next][1]

# print(d)

# print(max(d))

'''
시도2 : 탑다운
'''

n = int(input())
table = [(0,0)]

d = [0] * 16

for i in range(n):
    t, p = map(int, input().split())
    table.append((t,p))

# print(table)

for i in range(n, 0, -1):

    if i + table[i][0] <= n+1:
        d[i] = table[i][1]
        next = i + table[i][0]
        # next = 9
    else:
        continue
    max_num = 0
    if next <= n:
        for idx in range(next,n+1):
            if d[idx] > max_num:
                max_num = d[idx]
        d[i] += max_num

# print(d)
print(max(d)) 