import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
N, M = map(int, input().split())
w_size = list(map(int, input().split()))

dp = [1 << 30] * (N + 1)


def recur(total):
    if total < 0:
        return 10000000
    elif total == 0:
        return 0

    if dp[total] != 1 << 30:
        return dp[total]

    for i in range(M):
        dp[total] = min(dp[total], recur(total - w_size[i]) + 1)
        for j in range(i + 1, M):
            dp[total] = min(dp[total], recur(total - w_size[i] - w_size[j]) + 1)

    return dp[total]


ans = recur(N)
if ans >= 10000000:
    print(-1)
else:
    print(ans)


# import math
# from collections import defaultdict, deque

# n, m = map(int, input().split())
# s = list(map(int, input().split()))
# s.reverse()

# wok = defaultdict(int)
# for ss in s:
#     wok[ss] += 1

# print(wok)

# # 전체 요리한 합이 n이면 되는거자나?

# temp = []

# def backtracking():

#     if sum(temp) == n:
#         return True
    
#     if sum(temp) > n:
#         return False
    
#     for i in range(m):
#         temp.append(s[i])
#         result = backtracking()
#         if result:
#             return temp
#             # print(math.ceil(len(temp) / 2))
#             # exit()
#         temp.pop()

# result = backtracking()
# print(result)

# queue = deque(temp)
# temp2 = []
# count = 0
# check = 1
# while queue:
#     check += 1
#     if len(temp2) < 2:
#         wokwok = queue.popleft()
#         if wok[wokwok] > 0:
#             temp2.append(wokwok)
#             wok[wokwok] -= 1
#         else:
#             queue.append(wokwok)

#     if check >= len(temp):
#         count += 1
#         temp2.clear()

#     if len(temp2) == 2:
#         count += 1
#         wok[temp2[0]] += 1
#         wok[temp2[1]] += 1
#         temp2.clear()

# if temp2:
#     count += 1

# if count == 0:
#     print(-1)
# else:
#     print(count)