'''
비트 마스킹 아직 이해가 잘 안됨..ㅠ_ㅠ
'''

import sys
from itertools import combinations
input = sys.stdin.readline
n, m = map(int, input().split())

music = {}
guitars = set()

for _ in range(n):
    instrument, song = input().split()
    guitars.add(instrument)

    song = song.replace("Y", "1").replace("N", "0")
    music[instrument] = int(song, 2)
print(music)

max_cnt, max_guitar = 0, 0

play = list(music.items())

# 비트마스킹
for i in range(1, n+1):
    for combi in combinations(play, i):
        two = 0
        for g, a in combi:
            two |= a
            
        count = 0
        for j in range(m):
            if two & (1 << j):
                count += 1

        if max_cnt < count:
            max_cnt = count
            max_guitar = i

if max_guitar != 0:
    print(max_guitar)
else:
    print(-1)



# import sys
# input = sys.stdin.readline
# from itertools import combinations

# n, m = map(int, input().split())
# check = [0] * m

# case = []
# for _ in range(n):
#     instrument, song = input().split()
#     # song = song.replace("Y", "1").replace("N", "0")
#     # print(song)
#     case.append([instrument, song])

# guitar = [0] * m
# result = sys.maxsize
# count = 0

# for i in range(1, n+1):
#     for combi in combinations(case, i):


# def backtracking(start):
#     global count, result
#     if sum(check) == m:
#         result = min(result, count)
#         return
    
#     for i in range(start, n):
#         for j in range(m):
#             if case[i][1][j] == "Y":
#                 check[j] = 1
#                 guitar[j] += 1
#         count += 1
#         backtracking(start+1)
#         count -= 1
#         for k in range(m):
#             if case[i][1][k] == "Y":
#                 check[k] = 0
#                 guitar[k] -= 1

# backtracking(0)

# if result == sys.maxsize:
#     print(-1)
# else: print(result)

# check = [0] * m
# result = sys.maxsize
# count = 0

# def backtracking(start):
#     global count, result
#     if sum(check) == m:
#         result = min(result, count)
#         count -= 1
#         return
    
#     for i in range(start, n):
#         for j in range(m):
#             if case[i][1][j] == "Y":
#                 check[j] = 1
#         count += 1
#         backtracking(start+1)
#         for j in range(m):
#             if case[i][1][j] == "Y":
#                 check[j] = 0

# backtracking(0)
# print(result)