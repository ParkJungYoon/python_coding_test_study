'''
티셔츠를 만드는 비용은 같은 조 내에서 (가장 키가 큰 원생 - 가장 키가 작은 원생)
최소 비용으로
'''

n, m = map(int, input().split())
kindergarten = list(map(int, input().split()))
difference = []
for i in range(1, n):
    difference.append(kindergarten[i] - kindergarten[i-1])

difference.sort()
print(sum(difference[:n-m]))