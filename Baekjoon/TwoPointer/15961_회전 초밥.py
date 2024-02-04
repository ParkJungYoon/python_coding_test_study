import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
cobab = [int(input()) for _ in range(n)]
check_coupon = False
cur_cobab = defaultdict(int)
answer = 0

cur_cobab[c] += 1

for i in range(k):
    cur_cobab[cobab[i]] += 1

for i in range(k,n+k):
    answer = max(answer, len(cur_cobab))
    if answer == d:
        break
    
    i = i % n
    cur_cobab[cobab[i-k]] -= 1
    # 초밥이 0개인 경우를 바로바로 지워주니깐 시간이 2736ms -> 668ms로 바뀜
    if cur_cobab[cobab[i-k]] == 0:
        del cur_cobab[cobab[i-k]]
    cur_cobab[cobab[i]] += 1

print(answer)