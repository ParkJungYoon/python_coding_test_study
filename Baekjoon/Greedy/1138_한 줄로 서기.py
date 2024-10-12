import sys
input = sys.stdin.readline

n = int(input())
left = list(map(int, input().split()))
position = [0] * n

for i in range(n):
    # 자신의 왼쪽에 키 큰 사람의 수
    zero_count = 0
    for j in range(n):
        # 자신의 왼쪽에 키 큰 사람의 수가 맞고 그 자리에 아무도 없다면
        if position[j] == 0 and zero_count == left[i]:
            position[j] = i + 1
            break
        if position[j] == 0:
            zero_count += 1
print(*position)