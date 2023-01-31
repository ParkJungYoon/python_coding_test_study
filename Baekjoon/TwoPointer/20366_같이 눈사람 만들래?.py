import sys
input = sys.stdin.readline

n = int(input())
numbers = sorted(list(map(int, input().split())))
min_num = sys.maxsize

for i in range(n-1):
    for j in range(i + 1, n):
        temp1 = numbers[i] + numbers[j]
        start = 0
        end = n - 1
        while start < end:
            if start == i or start == j:
                start += 1
                continue
            if end == i or end == j:
                end -= 1
                continue

            temp2 = numbers[start] + numbers[end]
            min_num = min(min_num, abs(temp1 - temp2))
            if temp2 < temp1:
                start += 1
            elif temp2 > temp1:
                end -= 1
            else:
                start += 1
                end -= 1

print(min_num)


# combi = list(combinations(numbers, 2))
# result = 1e9

# print(combi, result)
# for i in range(n):
#     for j in range(i, n):
#         if result > abs(sum(combi[i]) - sum(combi[j])):
#             result = abs(sum(combi[i]) - sum(combi[j]))

# print(result)