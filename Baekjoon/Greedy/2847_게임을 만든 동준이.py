import sys
input = sys.stdin.readline

n = int(input())
score = []
result = 0

for _ in range(n):
    score.append(int(input()))

for i in range(n-2, -1, -1):
    if score[i] >= score[i+1]:
        minus_count = score[i]-(score[i+1]-1)
        score[i] -= minus_count
        result += minus_count

print(result)