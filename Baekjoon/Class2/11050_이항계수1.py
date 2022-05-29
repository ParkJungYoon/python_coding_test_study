from itertools import combinations
n, k = list(map(int,input().split()))

result = list(combinations(range(n),k))
print(len(result))