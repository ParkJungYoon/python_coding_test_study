import sys
input = sys.stdin.readline

n, k = map(int, input().split())
card = list(map(int, input().split()))
d = list(map(int, input().split()))

def back_to_the_past(current_card):
    one_step = [0] * n
    for i in range(n):
        index = d[i]
        one_step[index-1] = current_card[i]
    return one_step

for _ in range(k):
    card = back_to_the_past(card)

print(*card)