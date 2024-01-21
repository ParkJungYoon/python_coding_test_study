import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

cur = 0
count = 0
answer = 0

'''
IOI가 몇 번 있는지로
'''

while cur < (m - 1):
    if s[cur:cur+3] == 'IOI': # P_1 으로 체크
        count += 1
        cur += 2
        if count == n:      # P_1이 n개가 되면 
            answer += 1     # P_n 갯수 증가
            count -= 1
    else:
        # cur부터 3개의 문자가 IOI 가 아니면 P_1 갯수 초기화
        count = 0
        cur += 1 

print(answer)

'''
def make_pn(n):
    temp = []
    length = 2 * n + 1
    for i in range(length):
        if i % 2 == 0:
            temp.append("I")
        else:
            temp.append("O")
    return ''.join(temp)

pn = make_pn(n)
nn = len(pn)
answer = 0

# 50점 코드
for i in range(m-nn+1):
    print(s[i:i+nn])
    if s[i:i+nn] == pn:
        answer += 1

print(answer)
'''