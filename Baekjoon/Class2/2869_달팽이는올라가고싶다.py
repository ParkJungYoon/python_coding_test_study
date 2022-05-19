import math
A, B, V = map(int,input().split())
result = math.ceil((V-B) / (A-B))
print(result)