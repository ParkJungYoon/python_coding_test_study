'''
똑같은 문제인데 범위가 더 커진 15961 회전초밥 풀이도 해보기
'''

import sys
input = sys.stdin.readline
from collections import defaultdict

n, d, k, c = map(int, input().split())
cobab = [int(input()) for _ in range(n)]
check_coupon = False
cur_cobab = defaultdict(int)
answer = 0

cur_cobab[c] += 1

'''
다시보니 쿠폰은 항상 존재할거니깐 +1 해두고 크기는 굳이 values 메서드로 호출안해도
바로 딕셔너리 크기 계산하면 된다.

def calc_number_of_things():
    cur_cobab[c] += 1
    # number = len([i for i in list(cur_cobab.values()) if i != 0])
    number = len(list(cur_cobab.values()))
    cur_cobab[c] -= 1
    return number
'''

for i in range(k):
    cur_cobab[cobab[i]] += 1

for i in range(k,n+k):
    answer = max(answer, len(cur_cobab))
    i = i % n
    cur_cobab[cobab[i-k]] -= 1
    # 초밥이 0개인 경우를 바로바로 지워주니깐 시간이 2736ms -> 668ms로 바뀜
    if cur_cobab[cobab[i-k]] == 0:
        del cur_cobab[cobab[i-k]]
    cur_cobab[cobab[i]] += 1

print(answer)
