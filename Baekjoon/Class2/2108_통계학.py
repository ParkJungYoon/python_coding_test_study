# 최빈값 시간 초과
# import statistics or statistics 모듈 사용
import sys
input = sys.stdin.readline
from collections import Counter
n = int(input())
num = [int(input()) for _ in range(n)]
num.sort()
# 산술평균
print(round(sum(num)/n))
nn = n // 2
# 중앙값
print(num[nn])
# 최빈값
mode = Counter(num).most_common()

if len(num) > 1 : 
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else : 
        print(mode[0][0])
else: 
    print(mode[0][0])

# 범위
print(num[-1]-num[0])